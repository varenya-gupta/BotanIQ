import wikipediaapi

user_agent = "BotanIQ/1.0 (varenyagupta412@gmail.com)"

def get_wikipedia_info(plant_name):
    # Initialize the Wikipedia API with specified user agent
    wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)

    # Fetch the page for the plant species
    page = wiki.page(plant_name)

    if not page.exists():
        print(f"Page for '{plant_name}' does not exist on Wikipedia.")
        return None

    # Extract summary and structure for storing sections
    info = {
        'title': page.title,
        'summary': page.summary,
        'sections': {}
    }

    # Recursive function to get all relevant sections and subsections
    def extract_sections(sections, content_dict):
        for section in sections:
            # Check for relevant keywords in the section titles
            if any(keyword in section.title.lower() for keyword in
                   ["care", "cultivation", "growing", "habitat", "indoor cultivation", "growing conditions", "Cultivation and uses", "Etymology", "Taxonomy", "Description", "Uses"]):
                # Ensure each section has a dictionary to separate text and subsections
                if section.title not in content_dict:
                    content_dict[section.title] = {}
                content_dict[section.title]['text'] = section.text

            # Recurse through subsections, creating a nested structure
            if section.sections:
                if section.title not in content_dict:
                    content_dict[section.title] = {}
                content_dict[section.title]['subsections'] = {}
                extract_sections(section.sections, content_dict[section.title]['subsections'])

    # Extract relevant sections and nested subsections
    extract_sections(page.sections, info['sections'])

    return info


# Function to save the output to a text file
def save_to_txt(file_path, plant_info):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Title: {plant_info['title']}\n")
        file.write(f"Summary: {plant_info['summary']}\n")
        file.write("Relevant Sections and Subsections:\n")

        # Recursive function to write the sections to the file
        def write_sections(content_dict, level=0):
            for title, content in content_dict.items():
                file.write(f"{' ' * level * 2}Section: {title}\n")
                if 'text' in content:
                    file.write(f"{' ' * (level + 1) * 2}Content: {content['text']}\n")
                if 'subsections' in content:
                    write_sections(content['subsections'], level + 1)

        write_sections(plant_info['sections'])



# Example usage
plant_name = ""  # Example plant name
plant_info = get_wikipedia_info(plant_name)

if plant_info:
    # Save the output to the input.txt file
    save_to_txt('z txt files/input.txt', plant_info)
    print("Information saved to input.txt.")
else:
    print("plant information not available")
