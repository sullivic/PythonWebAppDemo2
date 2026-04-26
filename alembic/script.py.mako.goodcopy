"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    category_table = op.create_table(
        "category",
        sa.Column("category_id", sa.Integer, nullable=False, primary_key=True, autoincrement=True),
        sa.Column("category_name", sa.String(128), nullable=False)
    )
    brand_table = op.create_table(
        "brand",
        sa.Column("brand_id", sa.Integer, nullable=False, primary_key=True, autoincrement=True),
        sa.Column("brand_name", sa.String(128), nullable=False)
    )
    product_table = op.create_table(
        "product",
        sa.Column("product_id", sa.Integer, nullable=False, primary_key=True, autoincrement=True),
        sa.Column("sku", sa.String(128), nullable=False),
        sa.Column("product_name", sa.String(128), nullable=False),
        sa.Column("product_description", sa.String(512), nullable=False),
        sa.Column("category_id", sa.Integer, nullable=False),
        sa.Column("brand_id", sa.Integer, nullable=False)
    )
    op.bulk_insert(
        category_table,
        [
            {"category_name":"Shoes"},
            {"category_name":"Spa Days"},
            {"category_name":"Hotels"},
            {"category_name":"Restaurants"}
        ]
    )
    op.bulk_insert(
        brand_table,
        [
            {"brand_name":"Nike"},
            {"brand_name":"Adidas"},
            {"brand_name":"Puma"},
            {"brand_name":"Reebok"},
            {"brand_name":"Dr Martens"},
            {"brand_name":"Champneys"},
            {"brand_name":"Ragdale Hall Spa"},
            {"brand_name":"Rudding Park Spa"},
            {"brand_name":"Thermae Bath Spa"},
            {"brand_name":"Eden Hall Day Spa"},
            {"brand_name":"Premier Inn"},
            {"brand_name":"Travelodge"},
            {"brand_name":"Holiday Inn"},
            {"brand_name":"Hilton Hotels"},
            {"brand_name":"Ibis"},
            {"brand_name":"Nandos"},
            {"brand_name":"Wagamamas"},
            {"brand_name":"Greggs"},
            {"brand_name":"Harvester"},
            {"brand_name":"Pizza Hut"}
        ]
    )
    op.bulk_insert(
        product_table,
        [
            {"sku":"S-81272837","product_name":"Nike Pegasus 41","product_description":"A reliable road-running staple featuring a ReactX foam midsole and dual Air Zoom units for a responsive, energised ride.", "category_id":1, "brand_id":1},
            {"sku":"S-81272838","product_name":"Adidas Adizero Adios Pro 4","product_description":"An elite racing shoe engineered with carbon-infused Energy Rods and Lightstrike Pro foam for maximum energy return during marathons.", "category_id":1, "brand_id":2},
            {"sku":"S-81272839","product_name":"Asics Gel-nimbus 28","product_description":"The lightest and most cushioned Nimbus yet, featuring advanced PureGEL technology and FF PLUS ECO foam for a plush, neutral stride.", "category_id":1, "brand_id":2},
            {"sku":"S-81272840","product_name":"New Balance Fresh Foam X 1080v14","product_description":"A flagship neutral trainer designed with a breathable mesh upper and dynamic updates to the Fresh Foam X midsole for long-distance comfort. Ubuy", "category_id":1, "brand_id":1},
            {"sku":"S-81272841","product_name":"Hoka Clifton 10","product_description":"A perennial bestseller with an increased 8mm heel-to-toe drop and 3mm of additional foam for a smoother, more padded landing on daily miles.", "category_id":1, "brand_id":4},
            {"sku":"S-81272842","product_name":"Saucony Endorphin Pro 4","product_description":"A high-performance racer combining PWRRUN HG and PB foams with a snappy carbon plate and Speedroll technology for race-day propulsion.", "category_id":1, "brand_id":2},
            {"sku":"S-81272843","product_name":"Brooks Ghost 17","product_description":"A dependable neutral trainer featuring nitrogen-infused DNA LOFT v3 cushioning and a redesigned heel collar for a secure, smooth transition.", "category_id":1, "brand_id":2},
            {"sku":"S-81272844","product_name":"Nike Vomero 18","product_description":"Nikes premier cushioned shoe for 2025, using a massive 46mm stack height of ZoomX and ReactX foams for ultimate impact protection.", "category_id":1, "brand_id":3},
            {"sku":"S-81272845","product_name":"On Cloudsurfer 2","product_description":"A cutting-edge trainer using CloudTec Phase technology for a seamless heel-to-toe transition and a high-fashion, athletic aesthetic. SVD", "category_id":1, "brand_id":3},
            {"sku":"S-81272846","product_name":"Puma Fast-R Nitro Elite 3","product_description":"A rule-breaking super shoe featuring a decoupled midsole, Nitro Elite foam, and a newly added lacing system for a customised, high-speed fit. Instagram", "category_id":1, "brand_id":3},
            {"sku":"S-81272847","product_name":"Asics Nova 5","product_description":"A high-energy trainer with a trampoline-inspired outsole and FF MAX foam, offering a bouncy feel for varied running paces. Frontrunner Athletics", "category_id":1, "brand_id":5},
            {"sku":"S-81272848","product_name":"Adidas Adizero Evo SL","product_description":"A versatile, affordable performance shoe inspired by elite racing flats, built for both speed workouts and everyday lifestyle wear. Ubuy", "category_id":1, "brand_id":5},
            {"sku":"S-81272849","product_name":"Hoka Bondi 9","product_description":"The most cushioned road shoe in the Hoka lineup, updated for 2025 with a lighter EVA foam and a roomier, more inclusive toe box. Foot District", "category_id":1, "brand_id":1},
            {"sku":"S-81272870","product_name":"Saucony Ride 18","product_description":"A versatile, value-driven daily trainer with upgraded PWRRUN+ foam and a durable rubber outsole for road and light trail usage", "category_id":1, "brand_id":1},
            {"sku":"S-81272871","product_name":"New Balance FuelCell Rebel v5","product_description":"A lightweight, non-plated trainer that uses a high-rebound FuelCell foam to provide a snappy, fast feel for tempo runs", "category_id":1, "brand_id":2},
            {"sku":"S-81272872","product_name":"Altra Lone Peak 9+","product_description":"A rugged trail runner with the signature zero-drop platform and a new ripstop material for improved durability on technical terrain", "category_id":1, "brand_id":5},
            {"sku":"S-81272873","product_name":"Nike Air Monarch 4","product_description":"The classic cross-training shoe featuring durable leather construction and full-length encapsulated Air-Sole units for all-day comfort", "category_id":1, "brand_id":1},
            {"sku":"S-81272874","product_name":"Adidas Runfalcon 5","product_description":"An accessible everyday trainer featuring a breathable mesh upper and Cloudfoam midsole for soft, dependable cushioning", "category_id":1, "brand_id":3},
            {"sku":"S-81272875","product_name":"Mizuno Neo Vista 2","product_description":"An innovative trainer with a smooth, rocker-style geometry and high-rebound midsole foam designed for effortless daily jogging. Ubuy", "category_id":1, "brand_id":2},
            {"sku":"S-81272876","product_name":"Brookes Glycerin 22","product_description":"A plush-ride specialist using new DNA Tuned midsole technology for dual-cell nitrogen-infused comfort on long, easy runs. WWD", "category_id":1, "brand_id":2},
            {"sku":"J-61272876","product_name":"Ultimate Zen Retreat","product_description":"A full-day immersive experience including a 90-minute hot stone massage, custom facial, and private access to the hydrotherapy pool", "category_id":2, "brand_id":6},
            {"sku":"J-61272877","product_name":"Midweek Morning Glow","product_description":"A 4-hour morning escape featuring a refreshing citrus body scrub, thermal suite access, and a nutritious two-course lunch", "category_id":2, "brand_id":8},
            {"sku":"J-61272878","product_name":"Couples Twilight Escape","product_description":"An evening package for two with side-by-side aromatherapy massages, champagne by the rooftop fire pit, and late-night pool access", "category_id":2, "brand_id":8},
            {"sku":"J-61272879","product_name":"Deep Tissue Recovery Day","product_description":"Specifically designed for athletes; includes a 60-minute deep tissue massage, cryotherapy session, and guided stretch workshop", "category_id":2, "brand_id":10},
            {"sku":"J-61272880","product_name":"Botanical Bliss Facial Day","product_description":"Focuses on skincare with a triple-cleanse organic facial, scalp massage, and take-home botanical serum gift set", "category_id":2, "brand_id":10},
            {"sku":"J-61272891","product_name":"Detox and De-stress Ritual","product_description":"Includes a full-body seaweed wrap, infrared sauna session, and a guided meditation track to use in our sensory lounge", "category_id":2, "brand_id":6},
            {"sku":"J-61272892","product_name":"Mother-to-be Gentle Care","product_description":"A nurturing day for expectant mums featuring a specialized prenatal massage, cooling leg treatment, and afternoon tea", "category_id":2, "brand_id":7},
            {"sku":"J-61272893","product_name":"The Gentlemans Grooming Day","product_description":"A tailored experience including a deep-cleansing facial, therapeutic back massage, and traditional hot towel shave", "category_id":2, "brand_id":8},
            {"sku":"J-61272894","product_name":"Lakeside Yoga and Spa","product_description":"Combines a 60-minute outdoor yoga flow with full access to lakeside saunas and a magnesium-infused mineral bath", "category_id":2, "brand_id":6},
            {"sku":"J-61272895","product_name":"Hammam Discovery Session","product_description":"An authentic Middle Eastern ritual featuring a traditional Kessa scrub, Rhassoul mud wrap, and mint tea ceremony", "category_id":2, "brand_id":9},
            {"sku":"J-61272896","product_name":"Holistic Healing Package","product_description":"A wellness-focused day including a 60-minute reflexology session, reiki healing, and access to the Himalayan salt room", "category_id":2, "brand_id":10},
            {"sku":"J-61272897","product_name":"Express Lunchtime Reviver","product_description":"A 90-minute taster package with a 25-minute back massage and a 25-minute express facial—perfect for busy professionals", "category_id":2, "brand_id":9},
            {"sku":"J-61272898","product_name":"Gold Leaf Luxury Experience","product_description":"Our premium tier, includes a 24k gold leaf facial, collagen body wrap, and a private butler for the thermal suite", "category_id":2, "brand_id":7},
            {"sku":"J-61272899","product_name":"Sound Bath and Sleep Ritual","product_description":"Focused on insomnia relief; features a 45-minute sound bowl meditation followed by a lavender-infused sleep massage", "category_id":2, "brand_id":7},
            {"sku":"J-61272900","product_name":"Vitamin C Brightening Day","product_description":"High-intensity glow treatment including a vitamin-infused body polish, facial, and fresh-pressed juice flight", "category_id":2, "brand_id":6},
            {"sku":"J-61272901","product_name":"Nordic Thermal Journey","product_description":"A self-guided circuit of ice plunges, Finnish saunas, and wood-fired hot tubs with a focus on circulation", "category_id":2, "brand_id":7},
            {"sku":"J-61272902","product_name":"Aromatherapy Garden Day","product_description":"Set in our outdoor pods; includes a choice of essential oil blends for a personalized 60-minute full-body treatment", "category_id":2, "brand_id":8},
            {"sku":"J-61272903","product_name":"Ayurvedic Balance Day","product_description":"Based on ancient Indian techniques; includes a Shirodhara oil treatment and a personalized Dosha-balancing consultation", "category_id":2, "brand_id":6},
            {"sku":"J-61272904","product_name":"Friends Pamper Party","product_description":"Group booking for 4+ people; includes mini-treatments, private lounge access, and bottomless prosecco for 2 hours", "category_id":2, "brand_id":9},
            {"sku":"J-61272905","product_name":"Signature Head-to-toe Ritual","product_description":"Our most popular all-rounder; includes a scalp massage, full body massage, and therapeutic foot soak", "category_id":2, "brand_id":9},
            {"sku":"M-61272910","product_name":"Standard King Room","product_description":"A spacious 30sqm room featuring a plush king-sized bed, ergonomic workstation, and walk-in rain shower", "category_id":3, "brand_id":11},
            {"sku":"M-61272911","product_name":"Executive Business Suite","product_description":"Includes separate living and sleeping areas, high-speed Wi-Fi, and exclusive access to the Club Lounge", "category_id":3, "brand_id":13},
            {"sku":"M-61272912","product_name":"Ocean-Front Deluxe","product_description":"Wake up to panoramic sea views from your private balcony, includes floor-to-ceiling windows and a marble bath", "category_id":3, "brand_id":14},
            {"sku":"M-61272913","product_name":"Family Interconnecting Wing","product_description":"Two linked bedrooms (1 King, 2 Twins) designed for families, featuring child-friendly amenities and extra storage", "category_id":3, "brand_id":12},
            {"sku":"M-61272914","product_name":"Honeymoon Penthouse","product_description":"Top-floor luxury with a private terrace hot tub, chilled champagne on arrival, and 24-hour butler service", "category_id":3, "brand_id":12},
            {"sku":"M-61272915","product_name":"Eco-Pod Garden Cabin","product_description":"Sustainable, minimalist lodging set in private woodlands with solar power and a wood-burning stove", "category_id":3, "brand_id":11},
            {"sku":"M-61272916","product_name":"Classic Double Room","product_description":"A cosy, traditional room perfect for short city breaks, featuring local artwork and premium linens", "category_id":3, "brand_id":11},
            {"sku":"M-61272917","product_name":"Wellness Spa Suite","product_description":"Features an in-room sauna, aromatherapy diffuser, and a yoga mat with pre-loaded guided meditation videos", "category_id":3, "brand_id":12},
            {"sku":"M-61272918","product_name":"Historic Loft Suite","product_description":"Located in the heritage wing with original exposed brickwork, high ceilings, and vintage-inspired decor", "category_id":3, "brand_id":13},
            {"sku":"M-61272919","product_name":"Presidential Grand Suite","product_description":"Our largest accommodation, including a dining room for eight, grand piano, and private security entrance", "category_id":3, "brand_id":15},
            {"sku":"M-61272920","product_name":"Accessible Queen Room","product_description":"Fully ADA-compliant room with widened doorways, grab rails, and a roll-in shower for maximum comfort", "category_id":3, "brand_id":14},
            {"sku":"M-61272921","product_name":"Pet-Friendly Garden Room","product_description":"Ground-floor room with direct access to a fenced patio; includes a designer pet bed and water bowls", "category_id":3, "brand_id":14},
            {"sku":"M-61272922","product_name":"The Artists Studio","product_description":"A creative-focused space with an easel, natural skylights, and a library of contemporary art books", "category_id":3, "brand_id":12},
            {"sku":"M-61272923","product_name":"Urban Studio Apartment","product_description":"Designed for long stays, featuring a fully equipped kitchenette, washer-dryer, and dining nook", "category_id":3, "brand_id":11},
            {"sku":"M-61272924","product_name":"Skyline View Junior Suite","product_description":"Elevated city views with a semi-private seating area and Nespresso coffee machine", "category_id":3, "brand_id":13},
            {"sku":"M-61272925","product_name":"Riverside Glamping Tent","product_description":"Luxury safari-style tent with a real bed, electricity, and private deck overlooking the riverbank", "category_id":3, "brand_id":11},
            {"sku":"M-61272926","product_name":"Digital Nomad Pod","product_description":"Soundproofed micro-room optimized for solo travellers, featuring a built-in desk and smart storage", "category_id":3, "brand_id":15},
            {"sku":"M-61272927","product_name":"Royal Heritage Chamber","product_description":"Traditional four-poster bed and antique furnishings within the castle’s original stone walls", "category_id":3, "brand_id":15},
            {"sku":"M-61272928","product_name":"Modernist Corner Suite","product_description":"Wraparound windows offering 270-degree views, featuring minimalist Scandi-style furniture", "category_id":3, "brand_id":14},
            {"sku":"M-61272928","product_name":"Courtyard View Twin","product_description":"Quiet, inward-facing room overlooking the Mediterranean garden, ideal for a peaceful nights rest", "category_id":3, "brand_id":12},
            {"sku":"A-61271200","product_name":"Chefs Table Experience","product_description":"An intimate 10-course tasting menu served directly at the kitchen counter with live interaction with the Head Chef", "category_id":4, "brand_id":16},
            {"sku":"A-61271201","product_name":"Standard Dining Table","product_description":"General reservation for breakfast, lunch, or dinner in our main dining hall", "category_id":4, "brand_id":17},
            {"sku":"A-61271202","product_name":"Al Fresco Terrace Table","product_description":"Outdoor seating under heated lamps, offering a relaxed atmosphere and views of the city square", "category_id":4, "brand_id":18},
            {"sku":"A-61271203","product_name":"Private Vault Dining","product_description":"A secluded table for up to 6 people located in our converted wine cellar; perfect for confidential meetings or celebrations", "category_id":4, "brand_id":18},
            {"sku":"A-61271204","product_name":"Traditional Afternoon Tea","product_description":"A classic service featuring hand-cut sandwiches, warm scones, and a selection of premium loose-leaf teas", "category_id":4, "brand_id":19},
            {"sku":"A-61271205","product_name":"Bottomless Brunch","product_description":"90 minutes of unlimited prosecco or mimosas paired with any two dishes from our curated brunch menu", "category_id":4, "brand_id":20},
            {"sku":"A-61271206","product_name":"Window Side Booth","product_description":"Elevated booth seating along our floor-to-ceiling windows, offering the best views of the waterfront", "category_id":4, "brand_id":20},
            {"sku":"A-61271207","product_name":"Sushi Bar Counter","product_description":"Front-row seating at the raw bar to watch our master sushi chefs prepare fresh omakase-style dishes", "category_id":4, "brand_id":17},
            {"sku":"A-61271208","product_name":"Sunday Roast Special","product_description":"A weekly tradition featuring slow-roasted meats, giant Yorkshire puddings, and seasonal vegetables", "category_id":4, "brand_id":19},
            {"sku":"A-61271209","product_name":"Garden Gazebo Table","product_description":"A private, romantic setup in our botanical garden; includes a floral centrepiece and candlelit service", "category_id":4, "brand_id":16},
            {"sku":"A-61271210","product_name":"Tapas and Wine Flight","product_description":"A guided tasting experience featuring five regional Spanish wines paired with artisanal small plates", "category_id":4, "brand_id":16},
            {"sku":"A-61271211","product_name":"Bar Counter Seating","product_description":"Casual, high-stool seating at the cocktail bar—ideal for solo diners or quick pre-theatre meals.", "category_id":4, "brand_id":20},
            {"sku":"A-61271212","product_name":"The Steakhouse Sampler","product_description":"A premium dinner package featuring three different cuts of dry-aged beef and a selection of signature sides", "category_id":4, "brand_id":18},
            {"sku":"A-61271213","product_name":"Seafood Platter for Two","product_description":"A grand display of lobster, oysters, mussels, and langoustines served on ice with traditional accompaniments", "category_id":4, "brand_id":17},
            {"sku":"A-61271214","product_name":"Vegan Gastronomy Night","product_description":"A monthly 6-course event showcasing plant-based techniques and seasonal heritage vegetables", "category_id":4, "brand_id":17},
            {"sku":"A-61271215","product_name":"The Family Feast","product_description":"Large-format platters served family-style in the center of the table, designed for groups of 4 to 8", "category_id":4, "brand_id":17},
            {"sku":"A-61271216","product_name":"Cocktail Masterclass and Nibbles","product_description":"Learn to shake three signature drinks with our lead mixologist, followed by a selection of sharing boards", "category_id":4, "brand_id":16},
            {"sku":"A-61271217","product_name":"Fireside Lounge Table","product_description":"Relaxed low-seating near the open hearth; perfect for evening drinks and small appetisers", "category_id":4, "brand_id":20},
            {"sku":"A-61271218","product_name":"Oyster and Champagne Bar","product_description":"A specialized reservation for fresh-shucked oysters and premium grower champagnes", "category_id":4, "brand_id":20},
            {"sku":"A-61271219","product_name":"Mezzanine Group Dining","product_description":"Overlooking the main hall, this semi-private space is ideal for corporate events or large social gatherings", "category_id":4, "brand_id":18}
        ]
    )
    op.create_foreign_key(
        'fk_category',
        'product', 'category',
        ['category_id'], ['category_id'],
    )
    op.create_foreign_key(
        'fk_brand',
        'product', 'brand',
        ['brand_id'], ['brand_id'],
    )


def downgrade() -> None:
    op.drop_table("product")
    op.drop_table("brand")
    op.drop_table("category")


