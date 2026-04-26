from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, scoped_session, relationship

from chromadb_operations import ChromaDatabaseOperations

# ---------- CONFIG ----------

DATABASE_URL = "mariadb+mariadbconnector://learnpy:mySQL12!\"@127.0.0.1:3306/learnpython1"

engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = scoped_session(
    sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
)


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "category"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    category_name: Mapped[str] = mapped_column(String(128), nullable=False)

    product: Mapped["Product"] = relationship(back_populates="category_children", cascade="all, delete-orphan")

    def to_dict(self):
        return {"category_id": self.category_id, "category_name": self.category_name}

    def __repr__(self):
        return f"Category(category_id={self.category_id}, category_name={self.category_name})"

class Brand(Base):
    __tablename__ = "brand"

    brand_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    brand_name: Mapped[str] = mapped_column(String(128), nullable=False)

    product: Mapped["Product"] = relationship(back_populates="brand_children", cascade="all, delete-orphan")

    def to_dict(self):
        return {"brand_id": self.brand_id, "brand_name": self.brand_name}

    def __repr__(self):
        return f"Brand(brand_id={self.brand_id}, brand_name={self.brand_name})"

class Product(Base):
    __tablename__ = "product"

    product_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    sku: Mapped[str] = mapped_column(String(128), nullable=False)
    product_name: Mapped[str] = mapped_column(String(128), nullable=False)
    product_description: Mapped[str] = mapped_column(String(512), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.category_id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.brand_id"))

    # 1-to-many: Product --> Category_Children
    category_children: Mapped[list["Category"]] = (
        relationship(back_populates="product"))

    # 1-to-many: Product --> Brand_Children
    brand_children: Mapped[list["Brand"]] = (
        relationship(back_populates="product"))

    def to_dict(self):
        return {"product_id": self.product_id, "sku": self.sku, "product_name": self.product_name, "product_description": self.product_description}

    def to_dict_ext(self):
#        cat_child_name = "DUMMY"
#        brand_child_name = "DUMMY"
        cat_child_name = self.category_children.category_name
        brand_child_name = self.brand_children.brand_name
        return {"product_id": self.product_id, "sku": self.sku, "product_name": self.product_name, "product_description": self.product_description, "category_name": cat_child_name, "brand_name": brand_child_name}

    def __repr__(self):
        return f"Product(product_id={self.product_id}, sku={self.sku}, product_name={self.product_name}, product_description={self.product_description})"

Base.metadata.create_all(engine)

chromaOps = ChromaDatabaseOperations()

app = Flask(__name__,
            static_url_path='',
            static_folder='static-content')
CORS(app)


@app.teardown_appcontext
def remove_session(exception=None):
    SessionLocal.remove()


# ---------- HELPERS ----------

def get_db():
    return SessionLocal()

# ---------- ROUTES ----------

@app.route("/categories", methods=["GET"])
def list_categories():
    db = get_db()
    categories = db.query(Category).all()
    return jsonify([cat.to_dict() for cat in categories])

@app.route("/brands", methods=["GET"])
def list_brands():
    db = get_db()
    brands = db.query(Brand).all()
    return jsonify([br.to_dict() for br in brands])

@app.route("/products", methods=["GET"])
def list_products():
    db = get_db()
    products = db.query(Product).all()
    return jsonify([pr.to_dict() for pr in products])

@app.route("/query_chroma_and_retrieve/<string:search_term>", methods=["GET"])
def query_chroma_and_retrieve(search_term):
    list_ids_id = chromaOps.query_chroma_retrieve(search_term)
    db = get_db()

    prs = db.query(Product).where(Product.product_id.in_(list_ids_id))

    return jsonify([pr.to_dict_ext() for pr in prs])

@app.route("/ingest_product_metadata_into_chroma", methods=["GET"])
def ingest_product_metadata_into_chroma():
    db = get_db()
    products = db.query(Product).all()
    ingest_all_sentences = []
    ingest_all_pks = []
    for pr in products:
        ingest_all_pks.append(str(pr.product_id))
        ingest_str = "%s %s" % (pr.product_name, pr.product_description)
        ingest_all_sentences.append(ingest_str)

    chromaOps.ingest_into_chroma(ingest_all_pks, ingest_all_sentences)

    return jsonify("Ingested correctly into chroma-database.")

if __name__ == "__main__":
    app.run(debug=True)
