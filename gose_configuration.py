from goose import Configuration
from goose.text import StopWords
from goose.parsers import Parser
from goose.parsers import ParserSoup
from goose.version import __version__

HTTP_DEFAULT_TIMEOUT = 30

AVAILABLE_PARSERS = {
    'lxml': Parser,
    'soup': ParserSoup,
}

class GoseConfiguration(Configuration):

    def __init__(self):
        # What's the minimum bytes for an image we'd accept is,
        # alot of times we want to filter out the author's little images
        # in the beginning of the article
        self.images_min_bytes = 4500

        # set this guy to false if you don't care about getting images,
        # otherwise you can either use the default
        # image extractor to implement the ImageExtractor
        # interface to build your own
        self.enable_image_fetching = False

        # set this valriable to False if you want to force
        # the article language. OtherWise it will attempt to
        # find meta language and use the correct stopwords dictionary
        self.use_meta_language = True

        # default language
        # it will be use as fallback
        # if use_meta_language is set to false, targetlanguage will
        # be use
        self.target_language = 'en'

        # defautl stopwrods class
        self.stopwords_class = StopWords

        # path to your imagemagick convert executable,
        # on the mac using mac ports this is the default listed
        self.imagemagick_convert_path = "/opt/local/bin/convert"

        # path to your imagemagick identify executable
        self.imagemagick_identify_path = "/opt/local/bin/identify"

        # used as the user agent that
        # is sent with your web requests to extract an article
        # self.browser_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2)"\
        #                         " AppleWebKit/534.52.7 (KHTML, like Gecko) "\
        #                         "Version/5.1.2 Safari/534.52.7"
        self.browser_user_agent = 'Goose/%s' % __version__

        # debug mode
        # enable this to have additional debugging information
        # sent to stdout
        self.debug = False

        # TODO
        self.extract_publishdate = None

        # TODO
        self.additional_data_extractor = None

        # Parser type
        self.available_parsers = AVAILABLE_PARSERS.keys()
        self.parser_class = 'lxml'

        # set the local storage path
        # make this configurable
        self.local_storage_path = ""

        self.http_timeout = HTTP_DEFAULT_TIMEOUT

