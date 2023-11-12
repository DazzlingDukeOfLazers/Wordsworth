
from src.noun_wrapper import NounWrapper
from src.english_dictionary_wrapper import EnglishDictionaryWrapper


def main():
    """The function `main` is the entry point of the program. It performs the following steps:
    
    1. Creates an instance of the `NounWrapper` class and an instance of the `EnglishDictionaryWrapper` class.
    2. Parses the command line arguments using the `parse_arguments` method of the `NounWrapper` instance and assigns the value of the `search` argument to the `search_term` variable.
    3. Searches for icons related to the `search_term` using the `search_icons` method of the `NounWrapper` instance and assigns the result to the `metadata` variable.
    4. If `metadata` is not `None`, it saves the metadata to a JSON file using the `save_metadata` method of the `NounWrapper` instance.
    5. Retrieves the ID of the first icon in the `metadata` and assigns it to the `icon_id` variable.
    6. Saves the SVG file of the icon using the `save_svg_file` method of the `NounWrapper` instance.
    7. Retrieves the definition of the `search_term` using the `get_definitions` method of the `EnglishDictionaryWrapper` instance and assigns it to the `definition` variable.
    8. Creates a dictionary `word_dict` with the keys "word" and "definition" and assigns the values of `search_term` and `definition[0]` respectively.
    9. Saves the `word_dict` to a file using the `save_dict` method of the `EnglishDictionaryWrapper` instance.
    
    Please note that this docstring is in Google format.
    """

    noun = NounWrapper()
    word_book = EnglishDictionaryWrapper()

    # get command line arguments
    args = noun.parse_arguments()
    search_term = args.search

    noun.search_and_save(search_term)

    # # get metadata from noun project
    # metadata = noun.search_icons(search_term, only_public_domain=1, thumbnail_size=42, include_svg=1, limit=1)
    # # metadata = noun.search_icons(search_term)

    # if metadata is not None:
    #     # save the metadata to a json file
    #     noun.save_metadata(search_term, metadata)

    #     icon_id = metadata["icons"][0]["id"]

    #     # save the svg file
    #     noun.save_icon_to_file(search_term, icon_id, file_format="png")

    #     definition = word_book.get_definitions(search_term)
    #     word_dict = {"word": f"{search_term}",
    #                  "definition": f"{definition[0]}"}
    #     word_book.save_dict(word_dict)


if __name__ == "__main__":
    main()
