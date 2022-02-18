
from datetime import datetime
import feedparser
import smtplib
from email.message import EmailMessage

sources = [
    {
        'name': '南大新聞',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=Media'
    },
    {
        'name': '招生訊息',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=Admission'
    },
    {
        'name': '學術研究',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=RnD'
    },
    {
        'name': '活動快遞',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=ACT'
    },
    {
        'name': '徵人啟事',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=Recruit'
    },
    {
        'name': '課程異動',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=CourseUp'
    },
    {
        'name': '最新消息',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=ALL'
    },
    {
        'name': '精緻師培',
        'rss': 'https://campus.nutn.edu.tw/newsPost3/rssNews.aspx?b=907'
    }
]

categoryBgcolorClass = {
    '南大新聞': 'bg1',
    '招生訊息': 'bg2',
    '學術研究': 'bg3',
    '活動快遞': 'bg4',
    '徵人啟事': 'bg5',
    '課程異動': 'bg6',
    '最新消息': 'bg7',
    '精緻師培': 'bg8',
}

currentDatetime = datetime.now()
items = []

for source in sources:
    rssContents = feedparser.parse(source['rss'])

    for rssContent in rssContents['entries']:
        published = datetime.strptime(rssContent['published'], '%a, %d %b %Y %H:%M:%S %Z')

        # Item published less than or eqaul to 65 minutes.
        if (currentDatetime - published).total_seconds() <= 3900:
            items.append({
                'category': source['name'],
                'title': rssContent['title'],
                'link': rssContent['link'],
                'published': published.strftime('%Y %m.%d<br />%H:%M:%S')
            })

if len(items) > 0:
    mailContent = """
    <html>
        <body>
            <header>
                <h1>南大公告推播</h1>
            </header>
            
            <table>
                <tr>
                    <th class="news_category_cell" colspan="2">公告</th>
                    <th class="news_published_cell">發布時間</th>
                </tr>
    """

    for item in items:
        mailContent += '<tr><td class="news_category_cell"><span class="news_category_text ' + categoryBgcolorClass[item['category']] + '">' + item['category'] + '</span></td>'
        mailContent += '<td class="news_title_cell"><a href="' + item['link'] + '">' + item['title'] + '</a></td><td class="news_published_cell">' + item['published'] + '</td></tr>'

    mailContent += """
            </table>

            <style>

                body
                {
                    margin: 0px auto;
                    width: 1024px;
                }

                header h1
                {
                    margin: 20px 0px 40px;
                    font-size: 30px;
                    letter-spacing: 5px;
                    text-align: center;
                }

                a:link,
                a:visited
                {
                    border-bottom: 1px solid transparent;
                    color: #000000;
                    text-decoration: none;
                }

                a:hover,
                a:active
                {
                    border-bottom: 1px solid #000000;
                }

                table
                {
                    width: 100%;
                    border-collapse: collapse;
                }

                th, td
                {
                    padding: 10px;
                    font-size: 20px;
                    font-weight: normal;
                }

                th
                {
                    border-bottom: 1px solid #000000;
                    letter-spacing: 5px;
                }

                td
                {
                    border-bottom: 1px solid #a4a3a3;
                }

                .news_category_cell
                {
                    padding-right: 0px;
                    min-width: 100px;
                }

                .news_category_text
                {
                    padding: 5px 10px;
                    background-color: #505050;
                    border-radius: 10px;
                    color: #ffffff;
                    font-size: 18px;
                }

                .news_title_cell
                {
                    line-height: 1.7;
                }

                .news_published_cell
                {
                    min-width: 130px;
                    text-align: center;
                }

                .bg1
                {
                    background-color: #C425A3;
                }

                .bg2
                {
                    background-color: #F9A02B;
                }

                .bg3
                {
                    background-color: #B8980A;
                }

                .bg4
                {
                    background-color: #2EBA3E;
                }

                .bg5
                {
                    background-color: #2C9DA7;
                }

                .bg6
                {
                    background-color: #2C48A7;
                }

                .bg7
                {
                    background-color: #D82F2F;
                }

                .bg8
                {
                    background-color: #8F3A84;
                }

            </style>
        </body>
    </html>
    """

    mail = EmailMessage()
    mail.set_content(mailContent, subtype='html')
    mail['To'] = 'user@example.com'
    mail['From'] = 'sender@example.com'
    mail['Subject'] = '南大公告推播 (僅蒐集65分鐘內的公告)'

    mailServer = smtplib.SMTP('localhost')
    mailServer.send_message(mail)
    mailServer.quit()

