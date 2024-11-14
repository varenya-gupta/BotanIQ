from species import detect_plants
from wiki import *
from TogetherAI import *

# Define plant names and their corresponding Wikipedia titles
plant_wikipedia_titles = {
    'African Violet (Saintpaulia ionantha)': 'Saintpaulia',
    'Aloe Vera': 'Aloe vera',
    'Anthurium (Anthurium andraeanum)': 'Anthurium andraeanum',
    'Areca Palm (Dypsis lutescens)': 'Dypsis lutescens',
    'Asparagus Fern (Asparagus setaceus)': 'Asparagus setaceus',
    'Begonia (Begonia spp.)': 'Begonia',
    'Bird of Paradise (Strelitzia reginae)': 'Strelitzia reginae',
    'Birds Nest Fern (Asplenium nidus)': 'Asplenium nidus',
    'Boston Fern (Nephrolepis exaltata)': 'Nephrolepis exaltata',
    'Calathea': 'Calathea',
    'Cast Iron Plant (Aspidistra elatior)': 'Aspidistra elatior',
    'Chinese Money Plant (Pilea peperomioides)': 'Pilea peperomioides',
    'Chinese evergreen (Aglaonema)': 'Aglaonema',
    'Christmas Cactus (Schlumbergera bridgesii)': 'Schlumbergera',
    'Chrysanthemum': 'Chrysanthemum',
    'Ctenanthe': 'Ctenanthe',
    'Daffodils (Narcissus spp.)': 'Narcissus (plant)',
    'Dracaena': 'Dracaena (plant)',
    'Dumb Cane (Dieffenbachia spp.)': 'Dieffenbachia',
    'Elephant Ear (Alocasia spp.)': 'Alocasia',
    'English Ivy (Hedera helix)': 'Hedera helix',
    'Hyacinth (Hyacinthus orientalis)': 'Hyacinthus orientalis',
    'Iron Cross begonia (Begonia masoniana)': 'Begonia masoniana',
    'Jade plant (Crassula ovata)': 'Crassula ovata',
    'Kalanchoe': 'Kalanchoe',
    'Lilium (Hemerocallis)': 'Hemerocallis',
    'Lily of the valley (Convallaria majalis)': 'Convallaria majalis',
    'Money Tree (Pachira aquatica)': 'Pachira aquatica',
    'Monstera Deliciosa (Monstera deliciosa)': 'Monstera deliciosa',
    'Orchid': 'Orchidaceae',
    'Parlor Palm (Chamaedorea elegans)': 'Chamaedorea elegans',
    'Peace lily': 'Spathiphyllum',
    'Poinsettia (Euphorbia pulcherrima)': 'Euphorbia pulcherrima',
    'Polka Dot Plant (Hypoestes phyllostachya)': 'Hypoestes phyllostachya',
    'Ponytail Palm (Beaucarnea recurvata)': 'Beaucarnea recurvata',
    'Pothos (Ivy arum)': 'Epipremnum aureum',
    'Prayer Plant (Maranta leuconeura)': 'Maranta leuconeura',
    'Rattlesnake Plant (Calathea lancifolia)': 'Calathea lancifolia',
    'Rubber Plant (Ficus elastica)': 'Ficus elastica',
    'Sago Palm (Cycas revoluta)': 'Cycas revoluta',
    'Schefflera': 'Schefflera',
    'Snake plant (Sansevieria)': 'Dracaena trifasciata',
    'Tradescantia': 'Tradescantia',
    'Tulip': 'Tulip',
    'Venus Flytrap': 'Venus flytrap',
    'Yucca': 'Yucca',
    'ZZ Plant (Zamioculcas zamiifolia)': 'Zamioculcas'
}

# Define the model path and image input
model_input = "work models/m2.pt"
image_input = r"C:\Users\nalin\Videos\iVCam\20241114003726.jpg"

# Detect plants
detected_plants = detect_plants(image_input, model_input)

# Initialize the list to hold Wikipedia titles for detected plants
wiki_detected_name = []

# Iterate directly over each plant name in detected_plants
for plant in detected_plants:
    # Handle common naming inconsistencies by checking multiple variations
    plant_title = plant_wikipedia_titles.get(plant)

    if plant_title is None:
        # Handle minor name mismatches or typos (for example, "Sanseviera" -> "Sansevieria")
        plant_title = plant_wikipedia_titles.get(plant.replace('Sanseviera', 'Sansevieria'))

    wiki_detected_name.append(plant_title)

print("Detected Plants with Wikipedia Titles:", wiki_detected_name)

# Now you can proceed with wiki_detected_name as needed
if wiki_detected_name:
    plant_name = wiki_detected_name[0]  # Use the first detected plant name
    plant_info = get_wikipedia_info(plant_name)

    if plant_info:
        # Save the output to the input.txt file
        save_to_txt('variable text files/input.txt', plant_info)
        print("Information saved to input.txt.")
    else:
        print("Plant information not available.")

Together_AI()
