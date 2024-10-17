import csv

# Function to load artworks and their associated artists from the CSV file
def load_artworks(filename):
    artworks = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming the CSV contains all necessary fields
            artworks[row['title']] = {
                'creation_date': row['creation_date'],
                'medium': row['medium'],
                'accession_number': row['accession_number'],
                'credit_line': row['credit_line'],
                'date_acquired': row['date_acquired'],
                'physical_location': row['physical_location'],
                'item_width': row['item_width'],
                'item_height': row['item_height'],
                'image_url': row['image_url'].split('|'),  # Assuming multiple URLs are pipe-separated
                'artists': row['artist_ids'].split('|')  # Assuming multiple artist IDs are pipe-separated
            }
    return artworks

# Function to interact with the user
def interactive_guide(artworks):
    print("Welcome to the Interactive Museum Artwork Guide!")
    while True:
        print("\nAvailable Artworks:")
        for artwork in artworks.keys():
            print(f"- {artwork}")
        print("Type 'exit' to quit.")
        
        user_input = input("Which artwork would you like to know about? ").strip()
        
        if user_input.lower() == 'exit':
            break
        
        if user_input in artworks:
            artwork_info = artworks[user_input]
            print(f"\nTitle: {user_input}")
            print(f"Creation Date: {artwork_info['creation_date']}")
            print(f"Medium: {artwork_info['medium']}")
            print(f"Accession Number: {artwork_info['accession_number']}")
            print(f"Credit Line: {artwork_info['credit_line']}")
            print(f"Date Acquired: {artwork_info['date_acquired']}")
            print(f"Physical Location: {artwork_info['physical_location']}")
            print(f"Dimensions: {artwork_info['item_width']} x {artwork_info['item_height']} inches")
            
            # Show the artwork images
            print("Images:")
            for img in artwork_info['image_url']:
                print(f"- {img}")  # Display image URLs (consider using a viewer for images in a GUI)
                
            # Display artist information
            print("Artists:")
            for artist_id in artwork_info['artists']:
                # Here we can assume we don't have artist details in a separate dictionary
                print(f"- Artist ID: {artist_id}")  # Display artist ID; you can customize this if you have more info.
            
            # Handle user questions about the artwork
            question_input = input("Ask a question about this artwork (or type 'back' to choose another): ")
            if question_input.lower() == 'back':
                continue
            
            # Provide a sample answer based on the artwork
            print(f"Here is some information about that question...")
            # Here, you can expand with actual logic to answer questions based on user input

        else:
            print("Artwork not found. Please try again.")

# Main program
if __name__ == "__main__":
    artworks = load_artworks('cmoa.csv')  # Load from the combined CSV file
    interactive_guide(artworks)