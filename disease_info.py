"""
Disease knowledge base providing symptoms, causes, and treatment advice
for all 38 classes in the PlantVillage dataset.
"""

from typing import Dict, Any

DISEASE_DATA: Dict[str, Dict[str, Any]] = {
    "Apple___Apple_scab": {
        "status": "Diseased",
        "description": "A serious fungal disease caused by Venturia inaequalis affecting apple foliage and fruit.",
        "symptoms": "Olive-green to dark brown or velvety black spots on leaves, leaf distortion, and scabby lesions on fruit.",
        "causes": "Prolonged leaf wetness during warm spring weather (55°F - 75°F).",
        "treatment": "Apply fungicides such as copper, captan, or myclobutanil early in the season. Rake and dispose of fallen infected leaves in autumn to reduce overwintering spores.",
        "prevention": "Prune trees to improve air circulation, plant resistant cultivars (e.g., Liberty, Freedom), and use drip irrigation to keep foliage dry."
    },
    "Apple___Black_rot": {
        "status": "Diseased",
        "description": "Fungal infection caused by Botryosphaeria obtusa leading to 'frogeye' leaf spot, fruit rot, and cankers on branches.",
        "symptoms": "Circular brown leaf spots with distinct purple borders ('frogeye'), sunken brown branch cankers, and rotting fruit with black pycnidia rings.",
        "causes": "Overwinters in dead wood and mummified fruit; favored by warm humid weather.",
        "treatment": "Prune out diseased twigs and remove all mummified fruit. Apply captan or sulfur-based fungicides during the growing season.",
        "prevention": "Sanitize pruning tools between cuts, avoid tree stress, and protect trees from insect damage."
    },
    "Apple___Cedar_apple_rust": {
        "status": "Diseased",
        "description": "A fungal disease caused by Gymnosporangium juniperi-virginianae that alternates between apple trees and eastern red cedar/juniper.",
        "symptoms": "Bright yellow-orange spots on leaves that turn reddish with black dots in the center; tube-like structures appear on leaf undersides in late summer.",
        "causes": "Presence of nearby juniper or cedar trees which harbor galls that release spores during spring rains.",
        "treatment": "Spray preventative fungicides containing myclobutanil, propiconazole, or sulfur from pink bud stage through petal fall.",
        "prevention": "Remove nearby eastern red cedar or juniper trees within a few hundred yards if possible; plant resistant apple varieties."
    },
    "Apple___healthy": {
        "status": "Healthy",
        "description": "The apple foliage appears vibrant, well-nourished, and free of visible fungal lesions or bacterial blight.",
        "symptoms": "Uniform green foliage, firm leaf structure, and healthy vegetative growth.",
        "causes": "Good cultural management, balanced fertilization, and adequate sunlight.",
        "treatment": "No disease treatment required.",
        "prevention": "Continue regular monitoring, maintain balanced tree nutrition, prune annually, and ensure proper watering."
    },
    "Blueberry___healthy": {
        "status": "Healthy",
        "description": "The blueberry plant displays healthy green foliage with no signs of fungal or nutrient deficiency issues.",
        "symptoms": "Glossy green leaves, strong shoots, and normal fruit set.",
        "causes": "Adequate soil acidity (pH 4.5 - 5.5) and good drainage.",
        "treatment": "No disease treatment required.",
        "prevention": "Maintain acidic soil pH using elemental sulfur or peat moss, mulch with pine needles or bark, and provide consistent moisture."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "status": "Diseased",
        "description": "A common fungal disease caused by Podosphaera clandestina affecting leaves and young twigs.",
        "symptoms": "White to grayish powdery coating on leaf surfaces, curling or crinkling of leaves, and stunted new shoot growth.",
        "causes": "High humidity combined with moderate temperatures and shaded foliage.",
        "treatment": "Spray horticultural oil, neem oil, or sulfur-based fungicides when symptoms first appear.",
        "prevention": "Prune dense canopies to promote sunlight penetration and air movement; avoid overhead watering."
    },
    "Cherry_(including_sour)___healthy": {
        "status": "Healthy",
        "description": "The cherry foliage is healthy, showing robust green coloration without mildew or leaf spot symptoms.",
        "symptoms": "Normal leaf shape, crisp green coloring, and healthy buds.",
        "causes": "Proper pruning, well-draining soil, and routine pest management.",
        "treatment": "No disease treatment required.",
        "prevention": "Continue standard orchard maintenance, weed control, and preventive dormant oil sprays in winter."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "status": "Diseased",
        "description": "Fungal disease caused by Cercospora zeae-maydis, one of the most yield-limiting corn foliar diseases worldwide.",
        "symptoms": "Rectangular, tan to grayish lesions bounded by leaf veins; lesions expand and merge, blighting entire leaves.",
        "causes": "Warm, humid conditions and reduced tillage systems where crop debris remains on the soil surface.",
        "treatment": "Foliar fungicides (strobilurins, triazoles) applied between VT (tasseling) and R2 (blister stage) when conditions favor disease spread.",
        "prevention": "Rotate crops with non-grasses (such as soybeans), practice tillage to bury residues, and choose resistant hybrids."
    },
    "Corn_(maize)___Common_rust_": {
        "status": "Diseased",
        "description": "Fungal disease caused by Puccinia sorghi that produces reddish-brown pustules on both upper and lower leaf surfaces.",
        "symptoms": "Small, powdery cinnamon-brown to dark rust-colored pustules across leaves that rupture the epidermis.",
        "causes": "Cool to moderate temperatures (60°F - 75°F) with high relative humidity or dew.",
        "treatment": "Apply fungicides if rust pustules appear on upper leaves before dent stage on susceptible hybrids.",
        "prevention": "Plant resistant hybrids; plant early to minimize exposure to spores blown in from southern regions."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "status": "Diseased",
        "description": "A destructive fungal leaf blight caused by Exserohilum turcicum causing large cigar-shaped lesions.",
        "symptoms": "Long, elliptical, grayish-green or tan lesions (1-6 inches long) shaped like cigars.",
        "causes": "Prolonged wet weather, moderate temperatures (65°F - 80°F), and infected corn stubble.",
        "treatment": "Apply recommended fungicides (triazoles or strobilurins) at tasseling stage if disease pressure is high.",
        "prevention": "Rotate crops, till infected residue into soil, and select resistant corn hybrids with Ht gene resistance."
    },
    "Corn_(maize)___healthy": {
        "status": "Healthy",
        "description": "The corn plant exhibits vigorous, dark green foliage with clear, intact veins and healthy leaf blades.",
        "symptoms": "Vibrant green leaves without spots, stripes, or lesions; sturdy stalk development.",
        "causes": "Balanced soil nitrogen, adequate moisture, and effective weed management.",
        "treatment": "No disease treatment required.",
        "prevention": "Maintain soil fertility, monitor for corn borer and rootworm, and ensure adequate spacing."
    },
    "Grape___Black_rot": {
        "status": "Diseased",
        "description": "Severe fungal disease caused by Phyllosticta ampelicida (Guignardia bidwellii) affecting all green parts of the vine.",
        "symptoms": "Circular reddish-brown leaf spots with black fruiting bodies; infected grapes shrivel into black, wrinkled mummies.",
        "causes": "Rainy weather and warm temperatures (70°F - 85°F). Overwinters in mummified berries and cankers.",
        "treatment": "Apply fungicides containing myclobutanil, captan, or mancozeb from bud break through veraison. Prune away all mummies.",
        "prevention": "Train vines for open canopies, manage ground weeds, and avoid overhead sprinkler irrigation."
    },
    "Grape___Esca_(Black_Measles)": {
        "status": "Diseased",
        "description": "A complex fungal trunk disease caused by Phaeomoniella chlamydospora and Fomitiporia species causing 'tiger-stripe' leaf patterns.",
        "symptoms": "Interveinal yellowing and necrosis resulting in a 'tiger-stripe' leaf look; dark spots on fruit ('measles') and sudden vine collapse.",
        "causes": "Fungi entering pruning wounds on mature grapevines.",
        "treatment": "There is no chemical cure once established in the trunk. Prune out dead cordons back to healthy white wood; apply wound sealants.",
        "prevention": "Delay pruning until late winter when vine wounds heal faster; disinfect pruning shears between vines."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "status": "Diseased",
        "description": "Foliar fungal infection caused by Pseudocercospora vitis (Isariopsis clavispora) causing late-season defoliation.",
        "symptoms": "Irregular dark brown or black spots with definite margins on leaves; severe infections cause premature leaf drop.",
        "causes": "High humidity and dense vine foliage, especially late in the growing season.",
        "treatment": "Copper or sulfur based fungicides applied mid-season can control leaf blight.",
        "prevention": "Improve canopy management to increase light and airflow; gather and compost fallen leaves after harvest."
    },
    "Grape___healthy": {
        "status": "Healthy",
        "description": "The grapevine foliage is lush, broad, and uniform in green color without blight or mildew.",
        "symptoms": "Healthy, well-developed grape leaves with strong tendrils and vigorous shoot growth.",
        "causes": "Optimal sun exposure, balanced irrigation, and good trellis training.",
        "treatment": "No disease treatment required.",
        "prevention": "Perform seasonal pruning, maintain weed-free vine rows, and monitor for early fungal signs."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "status": "Diseased",
        "description": "Huanglongbing (HLB) is one of the most destructive citrus diseases, caused by the bacterium Candidatus Liberibacter asiaticus.",
        "symptoms": "Asymmetrical blotchy mottling on leaves, yellow shoots, vein corking, small lopsided bitter fruit that fails to color properly.",
        "causes": "Transmitted by the Asian citrus psyllid (Diaphorina citri) or infected grafting budwood.",
        "treatment": "There is no cure once a tree is infected. Manage the Asian citrus psyllid vector with systemic insecticides; remove infected trees to protect the grove.",
        "prevention": "Use certified disease-free nursery trees; control psyllid populations with biological agents (Tamarixia radiata) or chemical controls."
    },
    "Peach___Bacterial_spot": {
        "status": "Diseased",
        "description": "Bacterial disease caused by Xanthomonas arboricola pv. pruni affecting leaves, twigs, and fruit.",
        "symptoms": "Angular, water-soaked purple or black leaf spots that drop out, leaving a 'shot-hole' appearance; fruit cracks and pits.",
        "causes": "Wind-driven rains, sandy soils, and warm temperatures.",
        "treatment": "Apply copper sprays during dormant season and oxytetracycline sprays during bloom and post-petal fall.",
        "prevention": "Plant resistant cultivars, avoid excessive nitrogen fertilization, and install windbreaks around sandy sites."
    },
    "Peach___healthy": {
        "status": "Healthy",
        "description": "The peach foliage shows smooth lanceolate leaves with vibrant green coloration and no shot-holes.",
        "symptoms": "Intact leaves without spotting or leaf curl; vibrant shoot growth.",
        "causes": "Regular dormant oil sprays, good canopy sunlight, and proper drainage.",
        "treatment": "No disease treatment required.",
        "prevention": "Apply protective copper sprays before bud swell to prevent peach leaf curl, thin fruit appropriately."
    },
    "Pepper,_bell___Bacterial_spot": {
        "status": "Diseased",
        "description": "Bacterial disease caused by Xanthomonas campestris pv. vesicatoria damaging bell pepper foliage and peppers.",
        "symptoms": "Small, circular to irregular water-soaked spots on leaves that turn brown with yellow halos; leaf drop causing sunscald on fruit.",
        "causes": "Warm, wet weather; splash dispersal from rain or overhead sprinklers.",
        "treatment": "Spray fixed copper mixed with mancozeb at the first sign of symptoms.",
        "prevention": "Use certified disease-free seed, rotate away from solanaceous crops for 2 years, and use drip irrigation."
    },
    "Pepper,_bell___healthy": {
        "status": "Healthy",
        "description": "The pepper plant foliage is deep green, sturdy, and showing active bloom or fruit set.",
        "symptoms": "Glossy, uniform leaves with no curling, spots, or yellowing.",
        "causes": "Even soil moisture, warm temperatures, and good phosphorus/potassium levels.",
        "treatment": "No disease treatment required.",
        "prevention": "Maintain consistent watering to prevent blossom end rot, mulch with straw, and stake plants for support."
    },
    "Potato___Early_blight": {
        "status": "Diseased",
        "description": "A common fungal disease caused by Alternaria solani affecting potato foliage and tubers.",
        "symptoms": "Circular brown to dark spots on older leaves displaying characteristic concentric rings ('target board' pattern).",
        "causes": "Warm temperatures (75°F - 85°F) with alternating wet and dry periods; plant stress.",
        "treatment": "Apply protectant fungicides like chlorothalonil, mancozeb, or copper soaps at early symptoms.",
        "prevention": "Rotate crops with non-solanaceous crops, avoid overhead watering, ensure adequate nitrogen, and remove crop debris."
    },
    "Potato___Late_blight": {
        "status": "Diseased",
        "description": "Devastating oomycete disease caused by Phytophthora infestans (the pathogen behind the Irish potato famine).",
        "symptoms": "Large, dark brown to black water-soaked lesions on leaves and stems with white moldy fungal growth on leaf undersides in high humidity.",
        "causes": "Cool (60°F - 70°F), damp, overcast weather with prolonged leaf moisture.",
        "treatment": "Immediately apply targeted late-blight fungicides (e.g., cymoxanil, mandipropamid, or copper). Destroy heavily infected plants to stop spore clouds.",
        "prevention": "Plant certified disease-free seed potatoes, destroy cull piles, eliminate volunteer potatoes, and avoid overhead watering."
    },
    "Potato___healthy": {
        "status": "Healthy",
        "description": "The potato plant displays lush, robust foliage without blight lesions or chlorosis.",
        "symptoms": "Crisp green compound leaves, vigorous stems, and normal flowering.",
        "causes": "Healthy seed stock, well-draining loose soil, and timely hilling.",
        "treatment": "No disease treatment required.",
        "prevention": "Hill soil around stems to protect developing tubers from sun and spores, mulch well, and scout weekly."
    },
    "Raspberry___healthy": {
        "status": "Healthy",
        "description": "The raspberry canes display healthy composite leaves with clear green coloring and no cane blight.",
        "symptoms": "Strong floricanes and primocanes, intact serrated leaves, and healthy blossom clusters.",
        "causes": "Well-aerated soil, adequate trellis support, and annual pruning of old canes.",
        "treatment": "No disease treatment required.",
        "prevention": "Prune out spent floricanes after fruiting, ensure good airflow between rows, and water at soil level."
    },
    "Soybean___healthy": {
        "status": "Healthy",
        "description": "The soybean plants display healthy trifoliate leaves with vibrant green color and strong pod development.",
        "symptoms": "Clean trifoliate leaves, no rust pustules or chlorotic mosaic patterns.",
        "causes": "Proper rhizobial nitrogen fixation, weed canopy suppression, and good soil pH.",
        "treatment": "No disease treatment required.",
        "prevention": "Scout for soybean aphids, practice regular crop rotation, and test soil for soybean cyst nematodes."
    },
    "Squash___Powdery_mildew": {
        "status": "Diseased",
        "description": "Fungal infection caused by Podosphaera xanthii covering squash and pumpkin leaves in white talc-like powder.",
        "symptoms": "White powdery fungal growth spreading across leaf surfaces and stems; leaves turn yellow, brown, and dry out prematurely.",
        "causes": "High humidity, shade, and crowded planting.",
        "treatment": "Spray potassium bicarbonate, neem oil, sulfur, or bio-fungicides (Bacillus subtilis) at the first trace of white spots.",
        "prevention": "Space squash plants widely for ventilation, plant powdery mildew resistant cultivars, and avoid watering late in the day."
    },
    "Strawberry___Leaf_scorch": {
        "status": "Diseased",
        "description": "Fungal disease caused by Diplocarpon earlianum damaging strawberry leaf efficiency.",
        "symptoms": "Small purple-to-brown spots that lack a white center; spots enlarge until entire leaf looks purplish, dries up, and appears scorched.",
        "causes": "Prolonged leaf wetness during warm humid spells.",
        "treatment": "Apply fungicides such as captan or copper after renovation or early spring.",
        "prevention": "Renovate beds after harvest, remove old dead leaves, plant on raised beds, and use drip tape instead of sprinklers."
    },
    "Strawberry___healthy": {
        "status": "Healthy",
        "description": "The strawberry plant shows healthy trifoliate leaves with serrated edges, bright green color, and active runner or crown growth.",
        "symptoms": "Deep green foliage, clear white flowers, and clean fruit development.",
        "causes": "Mulched soil (straw), balanced feeding, and consistent drip irrigation.",
        "treatment": "No disease treatment required.",
        "prevention": "Renew mulch annually, replace crowns every 3-4 years, and maintain weed-free beds."
    },
    "Tomato___Bacterial_spot": {
        "status": "Diseased",
        "description": "Bacterial disease caused by Xanthomonas species causing severe defoliation and fruit spotting on tomato crops.",
        "symptoms": "Small, dark, greasy or water-soaked spots on leaves that turn brown with yellow halos; black scab-like raised spots on tomatoes.",
        "causes": "High temperatures and frequent rains; spreads via splashing water and contaminated tools.",
        "treatment": "Apply fixed copper bactericides combined with mancozeb. Remove severely infected lower branches.",
        "prevention": "Use certified disease-free seeds, practice crop rotation, sanitize stakes and cages, and avoid handling wet plants."
    },
    "Tomato___Early_blight": {
        "status": "Diseased",
        "description": "Fungal disease caused by Alternaria solani starting on the lowest leaves and working upward.",
        "symptoms": "Dark brown circular spots on older leaves featuring concentric rings ('bullseye' or target pattern); leaves turn yellow and drop.",
        "causes": "Warm, humid conditions and soil splashing onto lower foliage during rain.",
        "treatment": "Spray chlorothalonil, copper fungicide, or serenade biofungicide. Trim off lower infected leaves up to 12-18 inches from ground.",
        "prevention": "Mulch soil under plants to prevent soil splash, stake or cage plants, rotate tomato beds every 2-3 years, and water at the base."
    },
    "Tomato___Late_blight": {
        "status": "Diseased",
        "description": "A destructive water mold disease caused by Phytophthora infestans capable of killing entire tomato vines in days.",
        "symptoms": "Large, irregular, water-soaked brown/black lesions on leaves and stems; greasy brown firm patches on fruit; white mold under leaves in humidity.",
        "causes": "Cool, wet, rainy weather; windblown spores from nearby infected potato or tomato fields.",
        "treatment": "Immediate preventative copper or targeted oomycete fungicides. Bag and dispose of infected plants immediately—do not compost.",
        "prevention": "Plant resistant tomato cultivars (e.g., Mountain Magic, Defiant, Jasper), provide wide spacing, and keep foliage dry."
    },
    "Tomato___Leaf_Mold": {
        "status": "Diseased",
        "description": "Fungal disease caused by Passalora fulva (Fulvia fulva), particularly common in high tunnels and greenhouses.",
        "symptoms": "Pale greenish-yellow spots on upper leaf surfaces; velvety olive-green to grayish fungal mold directly underneath on the lower leaf surface.",
        "causes": "High relative humidity (greater than 85%) and poor air movement.",
        "treatment": "Apply copper or chlorothalonil fungicides. Increase ventilation and spacing.",
        "prevention": "Ventilate greenhouses and tunnels, increase plant spacing, prune suckers, and use fans to circulate air."
    },
    "Tomato___Septoria_leaf_spot": {
        "status": "Diseased",
        "description": "Common foliar fungal disease caused by Septoria lycopersici attacking lower foliage first.",
        "symptoms": "Numerous small circular spots with dark brown margins and sunken grayish-white centers containing tiny black specks (pycnidia).",
        "causes": "Overwinters in plant debris and weeds (horsenettle); spreads via splashing water.",
        "treatment": "Apply copper or chlorothalonil fungicides every 7-10 days in wet conditions. Strip off affected lower leaves.",
        "prevention": "Mulch beds thoroughly, clean up garden debris at season's end, and avoid overhead watering."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "status": "Diseased",
        "description": "Infestation by Tetranychus urticae, microscopic arachnids that suck cell contents from tomato leaves.",
        "symptoms": "Fine yellow or bronze stippling on leaf surfaces, silken webbing between leaves and stems, leaves become dry and paper-like.",
        "causes": "Hot, dry, dusty weather conditions.",
        "treatment": "Spray insecticidal soap, neem oil, or horticultural oils on both upper and lower leaf surfaces. Introduce predatory mites (Phytoseiulus persimilis).",
        "prevention": "Keep plants adequately watered to avoid drought stress; rinse leaves occasionally with a forceful stream of water to knock off mites."
    },
    "Tomato___Target_Spot": {
        "status": "Diseased",
        "description": "Fungal disease caused by Corynespora cassiicola causing target-patterned lesions on leaves and fruit.",
        "symptoms": "Small brown spots that enlarge into circular lesions with light brown centers and dark concentric rings; lesions cause leaf shedding.",
        "causes": "Warm temperatures (68°F - 82°F) and prolonged high humidity.",
        "treatment": "Apply protective fungicides such as chlorothalonil, azoxystrobin, or copper hydroxide.",
        "prevention": "Ensure good crop spacing, prune lower foliage for airflow, and avoid overhead sprinkler systems."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "status": "Diseased",
        "description": "Severe viral disease (TYLCV) transmitted by the silverleaf whitefly (Bemisia tabaci).",
        "symptoms": "Upward curling and cupping of leaves, yellow margins (chlorosis), severe stunting of plant growth, and flower drop with no fruit set.",
        "causes": "Whiteflies feeding on tomato plants and transmitting the geminivirus.",
        "treatment": "There is no cure once infected. Remove and bag infected plants immediately to prevent whiteflies from spreading the virus.",
        "prevention": "Use yellow sticky traps to monitor whiteflies, apply insecticidal soap or neem oil to control whitefly nymphs, use reflective silver mulches, and plant TYLCV-resistant varieties."
    },
    "Tomato___Tomato_mosaic_virus": {
        "status": "Diseased",
        "description": "A highly stable, contagious tobamovirus (ToMV) that infects tomatoes and related crops.",
        "symptoms": "Mottled light and dark green mosaic patterns on leaves, leaf distortion ('shoestringing' or fern-like appearance), and internal browning of fruit.",
        "causes": "Mechanical transmission via contaminated hands, tools, pruning shears, or tobacco products.",
        "treatment": "No cure exists. Infected plants must be dug up and disposed of to prevent spreading through the garden.",
        "prevention": "Wash hands with soap and water after handling tobacco products, sanitize tools in 10% bleach or trisodium phosphate, and plant resistant seed varieties."
    },
    "Tomato___healthy": {
        "status": "Healthy",
        "description": "The tomato plant displays lush, deep green foliage, sturdy stems, and active flower or fruit clusters.",
        "symptoms": "No spots, curling, or chlorosis; strong indeterminate or determinate growth.",
        "causes": "Full sunlight (6-8+ hours), consistent watering, and balanced tomato fertilizer.",
        "treatment": "No disease treatment required.",
        "prevention": "Maintain staking/trellising, prune suckers for airflow, mulch heavily, and water evenly at the base."
    }
}


def get_disease_info(raw_class_name: str) -> Dict[str, Any]:
    """Retrieve disease information dictionary for a given raw class name."""
    if raw_class_name in DISEASE_DATA:
        return DISEASE_DATA[raw_class_name]
    
    # Fallback for unrecognized classes
    is_healthy = "healthy" in raw_class_name.lower()
    return {
        "status": "Healthy" if is_healthy else "Diseased",
        "description": "Plant health condition identified by model.",
        "symptoms": "Normal growth" if is_healthy else "Foliar discoloration or spots detected.",
        "causes": "Standard environmental conditions.",
        "treatment": "No treatment required." if is_healthy else "Inspect plant closely and isolate if necessary.",
        "prevention": "Maintain good cultural practices, sanitation, and watering."
    }
