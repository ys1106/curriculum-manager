
import json
import ssl
from urllib.request import Request, urlopen


def crawl(topic):
    """
    Github API 를 이용하여 topic과 관련된 repository 를 검색하는 기능
    :param topic: 연관된 topic 을 알고싶은 topic
    :return: { input topic : response topics }
    """
    # try:
    head = 'application/vnd.github.mercy-preview+json'  # topic 값을 깃헙에서 받기 위해서
    url = 'https://api.github.com/search/repositories?q=topic:'  # 깃헙 API를 이용하기 위해서
    # url = 'https://api.github.com/search/topics?q=java+is:featured'  # description 을 얻을 수 있다.
    context = ssl._create_unverified_context()  # https 통신이 아닌 http 로 통신하기 위해
                                                # django가 서버로 인식되어서 https일 경우 ssl error 가 발생
    request = Request(url + topic)  # urllib 의 curl 기능을 사용하기 위해 ( 입력받은 topic 과 연관된 레포 검색 )
    request.add_header('Accept', head)  # 위에 달아놓았던 헤더를 적용
    response = urlopen(request, context=context)  # urlopen 으로 rest 요청을 하고 값을 받는다.

    topic_dict = {}  # topic 의 검색 개수
    for f in json.load(response)['items']:
        for t in f['topics']:
            try:  
                topic_dict[t] += 1  # 일단 1 더해
            except:  # 안들어있으면
                topic_dict[t] = 1  # 1로 저장

    del topic_dict[topic]  # 검색한 topic 은 지워
    sorted_d = [f for f in sorted(topic_dict.items(), key=lambda x: x[1], reverse=True) if f[1] > 3]  # 3개 넘으면 봄
    return sorted_d  # 입력 topic 은 key로 결과 topics 는 value로 하여 dictionary return
    # except:
    # return {topic: None}

#  3개 이상의 topic 만 사용할 것!
