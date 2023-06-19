
from src.noun_wrapper import NounWrapper


def main():

    noun = NounWrapper()

    # get command line arguments
    args = noun.parse_arguments()
    search_term = args.search

    # get metadata from noun project
    metadata = noun.get_icon(search_term)
    
    if metadata is not None:
        # save the metadata to a json file
        noun.save_metadata(search_term, metadata)
        
        # save the svg file
        noun.save_icon_files(search_term, metadata["icons"][0]["icon_url"])

if __name__ == "__main__":
    main()

