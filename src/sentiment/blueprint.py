from jsonschema import validate, ValidationError
from werkzeug.exceptions import BadRequest
from flask import Blueprint, jsonify, request
from sentiment.sentiment import Sentiment
import json

blueprint = Blueprint('sentiment', __name__)

@blueprint.record_once
def record(setup_state):
    blueprint.Sentiment = Sentiment()
    testJson = json.loads(
        r"""
        {"title": "Hollywood writers’ strike halts production of ‘Stranger Things,’ ‘Severance,’ Marvel’s ‘Blade’", "description": "<p class=\"paragraph\"> The&nbsp;<b>2023 Writers Guild of America strike</b>&nbsp;is an&nbsp;<a href=\"https://en.wikipedia.org/wiki/Strike_action\">labor dispute</a>&nbsp;between the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Writers_Guild_of_America\">Writers Guild of America</a>&nbsp;(WGA) — representing 11,500 screenwriters&nbsp;— and the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Alliance_of_Motion_Picture_and_Television_Producers\">Alliance of Motion Picture and Television Producers</a>&nbsp;(AMPTP). It began at 12:01&nbsp;a.m.&nbsp;<a href=\"https://en.wikipedia.org/wiki/Pacific_Time_Zone\">PDT</a>&nbsp;on May 2, 2023. </p><p class=\"paragraph\"> The strike is the largest interruption to American television and film production since the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_television_in_the_United_States\">COVID-19 pandemic</a>&nbsp;in 2020, as well as the largest labor stoppage the WGA has performed since the&nbsp;<a href=\"https://en.wikipedia.org/wiki/2007%E2%80%9308_Writers_Guild_of_America_strike\">2007–08 strike</a>. </p><h2>Issues in the strike</h2><p class=\"paragraph\"> One of the main focus points in the labor dispute is the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Residual_(entertainment_industry)\">residuals</a>&nbsp;from&nbsp;<a href=\"https://en.wikipedia.org/wiki/Streaming_media\">streaming media</a>;<a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-hollywoodreporter/1235404087-6\">[5]</a>&nbsp;the WGA claims that AMPTP's share of such residuals has cut much of the writers' average incomes compared to a decade ago.<a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-7\">[6]</a><a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-8\">[7]</a>&nbsp;Writers also wanted&nbsp;<a href=\"https://en.wikipedia.org/wiki/Artificial_intelligence\">artificial intelligence</a>&nbsp;such as&nbsp;<a href=\"https://en.wikipedia.org/wiki/ChatGPT\">ChatGPT</a>&nbsp;to be used only as a tool that can help with research or facilitate script ideas and not as a tool to replace them </p><p class=\"paragraph\"> On May&nbsp;2, 2020, the latest Minimum Basic Agreement (MBA) became the collective bargaining agreement that covered most of the work done by WGA writers.<a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-wga/contracts/mba-11\">[10]</a><a href=\"https://en.wikipedia.org/wiki/2023_Writers_Guild_of_America_strike#cite_note-sagaftra/wgaamptp/strike-12\">[11]</a>&nbsp;The Minimum Basic Agreement was an agreement that established a minimum wage for television and film writers. In television, the Minimum Basic Agreement only applied to those who wrote for&nbsp;<a href=\"https://en.wikipedia.org/wiki/Television_broadcasting\">broadcast television</a>&nbsp;shows and not for&nbsp;<a href=\"https://en.wikipedia.org/wiki/Streaming_television\">streaming television</a>. This was very clear when comparing&nbsp;<a href=\"https://en.wikipedia.org/wiki/Late-night_talk_show\">late-night talk shows</a>&nbsp;that were produced for broadcast television, such as&nbsp;<i><a href=\"https://en.wikipedia.org/wiki/The_Late_Show_with_Stephen_Colbert\">The Late Show with Stephen Colbert</a></i>&nbsp;by&nbsp;<a href=\"https://en.wikipedia.org/wiki/CBS\">CBS</a>&nbsp;versus&nbsp;<i><a href=\"https://en.wikipedia.org/wiki/The_Problem_with_Jon_Stewart\">The Problem with Jon Stewart</a></i>&nbsp;produced for streaming by&nbsp;<a href=\"https://en.wikipedia.org/wiki/Apple_TV%2B\">Apple TV+</a>. The writers who worked for&nbsp;<i>The Problem</i>&nbsp;were not covered by the MBA and therefore had to negotiate individually with the streaming company for their pay, and as a result, they were paid less than writers who wrote for&nbsp;<i>The Late Show</i>&nbsp;while doing the same amount of work. This pattern held true with other shows in the two categories.&nbsp;The MBA expired on May&nbsp;1, 2023. </p><p class=\"paragraph\"> The WGA estimated that its proposals would yield writers about $429&nbsp;million a year, whereas the AMPTP's offer would yield $86&nbsp;million. </p><p class=\"paragraph\"> One disputed issue is the Guild wanting requirements for \"mandatory staffing\" and \"duration of employment\" terms to be added to their contract, which would require all shows to be staffed with a minimum number of writers for a minimum amount of time, \"whether needed or not\" per the AMPTP. </p><p class=\"paragraph\"> Another important proposal that the WGA is advocating for is to ensure each member of a writing team receives their own pension and their own health care funds. The AMPTP rejected this proposal and did not offer a counterproposal. At the same time, there was a tentative agreement between the WGA and AMPTP to have 0.5% of negotiated minimums for all WGA minimums shifted into pensions and health funds. </p><p class=\"paragraph\"> <chronohash class=\"chrono-hash-highlight\">#Strike</chronohash> </p>", "media": [{"html": "<blockquote class=\"twitter-tweet\"><p lang=\"en\" dir=\"ltr\">IF IT AN’T ON THE PAGE .. IT AN’T on the STAGE !! <br>Writing is the beginning and the end !</p>&mdash; Henry Winkler (@hwinkler4real) <a href=\"https://twitter.com/hwinkler4real/status/1653764896432050178?ref_src=twsrc%5Etfw\">May 3, 2023</a></blockquote>\n<script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>\n"}]}
        """
    )
    score = blueprint.Sentiment.cleanAndGetSentiment(testJson)
    print(score)

@blueprint.route('/sentiment', methods=['POST'])
def getSentiment():
    try:
        json = request.get_json(force=True)
        score = blueprint.Sentiment.cleanAndGetSentiment(json)
        return jsonify({'score': score})


    except (BadRequest, ValidationError) as e:
        print('Bad request', e)
        return 'Bad request', 400

    except Exception as e:
        print('Server error', e)
        return 'Server error', 500
