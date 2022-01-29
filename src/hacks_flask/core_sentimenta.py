# Imports the Google Cloud client library
import os


credentials = os.path.abspath('keys.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=credentials

from google.cloud import language_v1
import core_gmaps
def analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze

    The score of a document's sentiment indicates the overall emotion of a document.
    The magnitude of a document's sentiment indicates how much emotional content is present within the document,
    and this value is often proportional to the length of the document.

    read this:
    https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    # print(u"Language of the text: {}".format(response.language))
    return [response.document_sentiment.score, response.document_sentiment.magnitude]

def find_best_review(reviews):
    # find the review with a sentiment score greater than 0.5 with the highest magnitude
    best_review = None
    best_score = 0
    best_magnitude = 0

    for review in reviews:
        sentiments = analyze_sentiment(review['text'])
        if sentiments[0] > 0.5 and sentiments[1] > best_magnitude:
            best_review = review
            best_score = sentiments[0]
            best_magnitude = sentiments[1]

    return [best_review, best_score, best_magnitude]

print(find_best_review(core_gmaps.getLocationReviews("Whitney Museum of American Art")))