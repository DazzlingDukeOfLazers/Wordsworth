
from src.noun_wrapper import NounWrapper
from src.english_dictionary_wrapper import EnglishDictionaryWrapper


def main():

    noun = NounWrapper()
    word_book = EnglishDictionaryWrapper()

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

        definition = word_book.get_definitions(search_term)
        word_dict = {"word": f"{search_term}",
                     "definition": f"{definition[0]}"}
        word_book.save_dict(word_dict)


if __name__ == "__main__":
    main()
