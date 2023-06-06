import openai
from linebot.models import MessageEvent, QuickReply, MessageAction, QuickReplyButton,LocationSendMessage, TextMessage, PostbackEvent, TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from urllib.parse import parse_qsl
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler
from flask import request, abort
from flask import Flask
app = Flask(__name__)


line_bot_api = LineBotApi(
    'A3P+CgPcftY9fSg0c99QJJfF3K6JomfTMaGhlwMDOw1TE/GwfrCR5HI9QsmcTIyPcTUmdyKqgEsQ1xIVEpQwsM/4KfN6mAVscO3vGPxCWboSN7PQ3Fo0B4N9aTlKiJwNQ1QV1XS5GwnC/n9BOHVFkgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d433d3231a5a3aad38d009ae17132291')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '特色美食':
        try:
            message = TextSendMessage(
                text='請選擇你想選的地區',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="東南亞", text="東南亞")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="北亞", text="北亞")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="南亞", text="南亞")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="東亞", text="東亞")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="中亞", text="中亞")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="西亞", text="西亞")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '尋找美食':
        try:
            message = TextSendMessage(
                text='請選擇你所在的地區',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="台北市", text="台北市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="新北市", text="新北市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="新竹市", text="新竹市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="桃園市", text="桃園市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="台中市", text="台中市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="高雄市", text="高雄市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="台南市", text="台南市")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '台北市':
        try:
            message = TextSendMessage(
                text='請選擇您想吃哪個國家的料理',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="日式料理", text="日式料理")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="韓式料理", text="韓式料理")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="泰式料理", text="泰式料理")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="中式料理", text="中式料理")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="俄式料理", text="俄式料理")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="印度料理", text="印度料理")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '日式料理':
        try:
            message = TextSendMessage(
                text='請選擇你想吃什麼',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="壽司", text="壽司")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="拉麵", text="拉麵")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="蕎麥麵", text="蕎麥麵")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="丼飯", text="丼飯")
                        ),
               
                
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '壽司':
        try:
            message = LocationSendMessage(
                title='壽司郎 天母高島屋店',
                address='11148台北市士林區忠誠路二段55號大葉高島屋 台北天母2樓',
                latitude=25.111643,  # 緯度
                longitude=121.5289153  # 經度
            )
            
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '拉麵':
        try:
            message = LocationSendMessage(
                title='男子漢拉麵食堂-士林天母店',
                address='111台北市士林區德行東路210號',
                latitude=25.111643,  # 緯度
                longitude=121.5289153  # 經度
            )
            
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '丼飯':
        try:
            message = LocationSendMessage(
                title='壹捌捌丼飯188',
                address='111台北市士林區至誠路二段28號1樓',
                latitude=25.0506879,  # 緯度
                longitude=121.4237571  # 經度
            )
            
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '蕎麥麵':
        try:
            message = LocationSendMessage(
                title='正宗日式手工蕎麥麵 蕎菜',
                address='10491台北市中山區中山北路一段105巷15號',
                latitude=25.0507603,  # 緯度
                longitude=121.4855596  # 經度
            )
            
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == '使用說明':
        try:
            message = TextSendMessage(
                text="使用者您好，我是亞洲美食，\n以下是使用說明:\n\n1.如果您不知道今天吃什麼好，可以點選[美食轉盤]，會出現一個轉盤，點選轉盤後會出現某個國家的料理，您就可以選擇去吃那個國家的料理了。\n\n2.點選[特色美食]就會跳出按鈕，讓您選擇想要認識亞洲哪個地區哪個國家的美食後，就會跳出那個國家知名度最高的美食。\n\n3.如果您想要自己製作美食，就點選[美食食譜]，會出現一些按鈕讓您選擇想製作的美食，接著chat gpt就會告訴您如何去烹飪。\n\n4.點選[美食種類]您可以透過按鈕選擇想吃早點、主餐還是下午茶，就會跳出那個種類的美食以及推薦餐廳。\n\n5.點選[尋找美食]可以定位您想吃的那家餐廳的位子。"
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '美食種類':
        try:
            message = TextSendMessage(
                text='請選擇想吃的',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="早點", text="早點")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="主食", text="主食 ")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="下午茶", text="下午茶 ")
                        ),

                    ]
                )
            )

            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '東南亞':
        try:
            message = TextSendMessage(
                text='請選擇國家',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="越南", text="越南")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="緬甸", text="緬甸")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="泰國", text="泰國")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="新加坡", text="新加坡")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="馬來西亞", text="馬來西亞")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="菲律賓", text="菲律賓")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="柬埔寨", text="柬埔寨")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="印度尼西亞", text="印度尼西亞")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == "北亞":
        try:
            message = TextSendMessage(
                text='請選擇國家',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="俄羅斯", text="俄羅斯")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))
    elif mtext == "南亞":
        try:
            message = TextSendMessage(
                text='請選擇國家',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="印度", text="印度")
                        ),
                      
                        QuickReplyButton(
                            action=MessageAction(label="巴基斯坦", text="巴基斯坦")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == "西亞":
        try:
            message = TextSendMessage(
                text='請選擇國家',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="土耳其", text="土耳其")
                        ),
                    
                        QuickReplyButton(
                            action=MessageAction(label="以色列", text="以色列")
                        ),
                     
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '東亞':
        try:
            message = TextSendMessage(
                text='請選擇國家',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="韓國", text="韓國")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="中國", text="中國")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="日本", text="日本")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="蒙古", text="蒙古")
                        ),

                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))

    elif mtext == '中亞':
        try:
            message = TextSendMessage(
                text='請選擇國家',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="哈萨克斯坦", text="哈萨克斯坦")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="乌兹别克斯坦", text="乌兹别克斯坦")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="吉尔吉斯斯坦", text="吉尔吉斯斯坦")
                        ),

                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='發生錯誤！'))


    elif mtext == '哈萨克斯坦':
        sendCarousel0(event)
    elif mtext == '日本':
        sendCarousel(event)
    elif mtext == '韓國':
        sendCarousel1(event)
    elif mtext == '蒙古':
        sendCarousel2(event)
    elif mtext == "中國":
        sendCarousel3(event)
    elif mtext == "俄羅斯":
        sendCarousel4(event)
    elif mtext == "印度尼西亞":
        sendCarousel5(event)
    elif mtext == '主食':
        sendCarousel6(event)
    elif mtext == '新加坡':
        sendCarouse7(event)
    elif mtext == '馬來西亞':
        sendCarousel8(event)
    elif mtext == '菲律賓':
        sendCarousel9(event)
    elif mtext == '早點':
        sendCarousel10(event)
    elif mtext == '泰國':
        sendCarousel11(event)
    elif mtext == '緬甸':
        sendCarousel12(event)
    elif mtext == '越南':
        sendCarousel13(event)
    elif mtext == '柬埔寨':
        sendCarousel14(event)
    elif mtext == '下午茶':
        sendCarousel15(event)
    elif mtext == '乌兹别克斯坦':
        sendCarousel16(event)
    elif mtext == '吉尔吉斯斯坦':
        sendCarousel17(event)
    elif mtext == '印度共和國':
        sendCarousel18(event)
    elif mtext == '土耳其':
        sendCarousel19(event)
    elif mtext == '巴基斯坦':
        sendCarousel20(event)
    elif mtext == '以色列':
        sendCarousel20(event)
def sendCarousel21(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='以色列',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/0/0d/Uncooked_Falafel_and_Falafel_Press.jpg',
                        title='油炸鷹嘴豆餅',
                        text='فلافل',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E6%B2%B9%E7%82%B8%E9%B7%B9%E5%98%B4%E8%B1%86%E9%A4%85'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))
def sendCarousel20(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='巴基斯坦',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Chicken_Manchurian.JPG/1280px-Chicken_Manchurian.JPG',
                        title='巴基斯坦中式美食',
                        text='滿洲雞',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E5%B7%B4%E5%9F%BA%E6%96%AF%E5%9D%A6%E5%BC%8F%E4%B8%AD%E5%9C%8B%E8%8F%9C#%E6%AD%B7%E5%8F%B2'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))
def sendCarousel19(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='土耳其',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Ouzb%C3%A9kistan-Ravioli_%281%29.jpg/1280px-Ouzb%C3%A9kistan-Ravioli_%281%29.jpg',
                        title='突厥饅頭',
                        text='Manti',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E7%AA%81%E5%8E%A5%E9%A5%85%E9%A0%AD'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendCarousel18(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='印度共和國',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/c/cb/Samosachutney.jpg',
                        title='印度咖哩餃',
                        text='समोसा',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E5%8D%B0%E5%BA%A6%E5%92%96%E5%93%A9%E9%A4%83'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel17(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='吉尔吉斯斯坦',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Kumys-bottle.jpg/360px-Kumys-bottle.jpg',
                        title='馬奶酒',
                        text='馬奶酒',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/wiki/%E9%A9%AC%E5%A5%B6%E9%85%92'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel16(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='乌兹别克斯坦',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/c/c4/Tajik_plov.jpg',
                        title='抓飯',
                        text='香料飯',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E6%8A%93%E9%A5%AD'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel0(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='哈萨克斯坦',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/%D0%91%D0%B5%D1%88%D0%B1%D0%B0%D1%80%D0%BC%D0%B0%D0%BA.jpg/480px-%D0%91%D0%B5%D1%88%D0%B1%D0%B0%D1%80%D0%BC%D0%B0%D0%BA.jpg',
                        title='別什巴爾馬克',
                        text='бешбармак',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E5%88%AB%E4%BB%80%E5%B7%B4%E5%B0%94%E9%A9%AC%E5%85%8B'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='日本',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.foodnext.net/dispPageBox/getFile/GetImg.aspx?FileLocation=%2FPJ-FOODNEXT%2FFiles%2F&FileName=photo-08258-i.jpg',
                        title='壽司',
                        text='sushi',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E5%AF%BF%E5%8F%B8'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel1(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='韓國',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.vogue.com.tw/photos/5f928719c0cb41b1da477568/1:1/w_4640,h_4640,c_limit/%E7%9B%B4%E5%9C%96-%E9%9F%93%E5%BC%8F%E9%83%A8%E9%9A%8A%E9%8D%8B.jpg',
                        title='部隊鍋',
                        text='부대찌개',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E9%83%A8%E9%9A%8A%E9%8D%8B'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel2(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='蒙古',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Roast_Whole_Lamb.jpg/330px-Roast_Whole_Lamb.jpg',
                        title='烤全羊',
                        text='Roasted Lamb',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E7%83%A4%E5%85%A8%E7%BE%8A'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel3(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='中國',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Peking_Duck%2C_2014_%2802%29.jpg/390px-Peking_Duck%2C_2014_%2802%29.jpg',
                        title='北京烤鴨',
                        text='Peking duck',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E5%8C%97%E4%BA%AC%E7%83%A4%E9%B8%AD'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel4(event):
    try:
        message = TemplateSendMessage(
            alt_text='俄羅斯',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/d/df/Pelmeni_Russian.jpg',
                        title='俄國餃子',
                        text='西伯利亞餃子',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E4%BF%84%E5%9C%8B%E9%A4%83%E5%AD%90'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel5(event):
    try:
        message = TemplateSendMessage(
            alt_text='印度尼西亞',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Sate_Ponorogo.jpg/375px-Sate_Ponorogo.jpg',
                        title='沙嗲',
                        text='Sate',
                        actions=[
                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E6%B2%99%E5%97%B2'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel6(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='午餐',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.vogue.com.tw/photos/5f928719c0cb41b1da477568/1:1/w_4640,h_4640,c_limit/%E7%9B%B4%E5%9C%96-%E9%9F%93%E5%BC%8F%E9%83%A8%E9%9A%8A%E9%8D%8B.jpg',
                        title='部隊鍋',
                        text='부대찌개',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/568ab4312756dd60b2ff06b4-%E9%9F%93%E9%A3%9F%E6%9D%91'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://tokyo-kitchen.icook.network/uploads/recipe/cover/371220/7d13ce32b584701e.jpg',
                        title='韓式炸雞',
                        text='양념치킨',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/5726463b2756dd6742e65d18'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://img.ltn.com.tw/Upload/food/page/2016/02/11/160211-901-0-auYrT.jpg',
                        title='石鍋拌飯',
                        text='비빔밥',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/5c736da22261396a0341c7c7-%E5%9B%9B%E7%B1%B3%E5%A4%A7%E7%9F%B3%E9%8D%8B%E6%8B%8C%E9%A3%AF%E5%B0%88%E8%B3%A3'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://storage.googleapis.com/www-cw-com-tw/article/202101/article-5ff76e12dff12.jpg',
                        title='日式拉麵',
                        text='ラーメン',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/58d01aac2756dd602f419dde-Soba-Shinn-%E6%9F%91%E6%A9%98'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Thai_and_hoi_nan_chicken_in_half.jpg/1280px-Thai_and_hoi_nan_chicken_in_half.jpg',
                        title='海南雞飯',
                        text='Hainanese Chicken Rice',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/5d47afabd6895d2d95c511e1-%E6%9E%97%E8%A8%98%E6%B5%B7%E5%8D%97%E9%9B%9E%E9%A3%AF'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/7/74/Bakutteh.jpg',
                        title='肉骨茶',
                        text='Bak kut teh',
                        actions=[
                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/578fbf282756dd01dcf7d481-%E6%B1%A0%E5%85%88%E7%94%9F%E5%92%96%E5%93%A9%E5%B1%8B'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/4/48/Lechon.jpg',
                        title='菲律賓燒乳豬',
                        text='Lechon',
                        actions=[
                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/5f572a7f2756dd155d8e598b-Cres-Art-Philippine-'
                            ),

                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarouse7(event):  # 轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='新加坡',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Thai_and_hoi_nan_chicken_in_half.jpg/1280px-Thai_and_hoi_nan_chicken_in_half.jpg',
                        title='海南雞飯',
                        text='Hainanese Chicken Rice',
                        actions=[

                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E6%B5%B7%E5%8D%97%E9%9B%9E%E9%A3%AF'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel8(event):
    try:
        message = TemplateSendMessage(
            alt_text='馬來西亞',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/7/74/Bakutteh.jpg',
                        title='肉骨茶',
                        text='Bak kut teh',
                        actions=[
                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E8%82%89%E9%AA%A8%E8%8C%B6'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel9(event):
    try:
        message = TemplateSendMessage(
            alt_text='菲律賓',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/4/48/Lechon.jpg',
                        title='菲律賓燒乳豬',
                        text='Lechon',
                        actions=[
                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-hant/%E8%8F%B2%E5%BE%8B%E8%B3%93%E7%87%92%E4%B9%B3%E8%B1%AC'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel10(event):
    try:
        message = TemplateSendMessage(
            alt_text='早點',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/HMOEMhAaVIGBNVZPP40jU-cjlVBkIag4Ot7mZcqTXY1x9Z6sswLcNNu9vpznAkewaW1OcamMK2PRdXJuOAke9CgyDDyIlpkDQYg2hray-cI=s600',
                        title='香滿園',
                        text='滷肉飯',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/559db73ac03a103ee86c9ea4-%E9%A6%99%E6%BB%BF%E5%9C%92'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/g0ljv5jmaOgxEhpiUIoYoVaDNRPAPo_TR4uE81IE5_yLDmk5Ddm4v-t6mjwOfqNamyLJ42D7gxXGPAJI3eHSP_4fD5M0z_0bfoit8n72GQ4=s600',
                        title='津津豆漿店',
                        text='蛋餅',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/559d5a4ec03a103ee86c6845-%E6%B4%A5%E6%B4%A5%E8%B1%86%E6%BC%BF%E5%BA%97'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Spring_onion_pancake_2013.JPG/450px-Spring_onion_pancake_2013.JPG',
                        title='忠誠山東葱油餅(此燈亮有餅)',
                        text='蔥油餅',
                        actions=[

                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/55a65193c03a104df53c9980-%E5%BF%A0%E8%AA%A0%E5%B1%B1%E6%9D%B1%E8%91%B1%E6%B2%B9%E9%A4%85-%E6%AD%A4%E7%87%88%E4%BA%AE%E6%9C%89%E9%A4%85-'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cc.tvbs.com.tw/img/upload/2020/08/06/20200806104431-ef6a22ee.jpg',
                        title='豆漿燒餅店',
                        text='燒餅油條',
                        actions=[
                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/5e9db0522756dd503a8baec3-%E8%B1%86%E6%BC%BF%E7%87%92%E9%A4%85%E5%BA%97'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel11(event):
    try:
        message = TemplateSendMessage(
            alt_text='泰國',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Basil_fried_crispy_pork_with_rice_-_Chiang_Mai_-_2017-07-11_%28002%29.jpg/1280px-Basil_fried_crispy_pork_with_rice_-_Chiang_Mai_-_2017-07-11_%28002%29.jpg',
                        title='打拋豬肉飯',
                        text='Phat kaphrao',
                        actions=[
                            URITemplateAction(
                                label='詳情資料',
                                uri='https://en.wikipedia.org/wiki/Phat_kaphrao'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel12(event):
    try:
        message = TemplateSendMessage(
            alt_text='緬甸',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Mohnga.jpg/330px-Mohnga.jpg',
                        title='魚湯麵',
                        text='မုန့်ဟင်းခါ',
                        actions=[
                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-tw/%E9%AD%9A%E6%B9%AF%E9%BA%B5'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel13(event):
    try:
        message = TemplateSendMessage(
            alt_text='越南',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Canhchua2.jpg/375px-Canhchua2.jpg',
                        title='越南酸湯',
                        text='Canh chua',
                        actions=[
                            URITemplateAction(
                                label='詳情資料',
                                uri='https://en.wikipedia.org/wiki/Canh_chua'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel14(event):
    try:
        message = TemplateSendMessage(
            alt_text='柬埔寨',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/f/f6/Amok_trey_khmer.jpg',
                        title='阿莫克',
                        text='amok trey',
                        actions=[
                            URITemplateAction(
                                label='詳情資料',
                                uri='https://zh.wikipedia.org/zh-hant/%E6%9F%AC%E5%9F%94%E5%AF%A8%E9%A3%B2%E9%A3%9F'
                            ),

                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendCarousel15(event):
    try:
        message = TemplateSendMessage(
            alt_text='下午茶',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Imagawayaki_001.jpg/640px-Imagawayaki_001.jpg',
                        title='伍饌道車輪餅',
                        text='紅豆餅',
                        actions=[
                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/61de3a5bcd99574a83484591-%E4%BC%8D%E9%A5%8C%E9%81%93%E8%BB%8A%E8%BC%AA%E9%A4%85'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.tony60533.com/wp-content/uploads/pixnet/1436708273-3019858402.jpg',
                        title='春美冰菓室',
                        text='珍珠奶茶冰',
                        actions=[
                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/59da68652756dd1e8b1954c8-%E6%98%A5%E7%BE%8E%E5%86%B0%E8%8F%93%E5%AE%A4'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://img.ltn.com.tw/Upload/playing/page/2019/04/13/190413-17482-3-114.jpg',
                        title='Ctrl+F Brunch & Cafe',
                        text='泰式打拋雞肉三明治可頌',
                        actions=[
                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/59f375772756dd26326731c3-Ctrl-F-Brunch-Cafe'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://img.ltn.com.tw/Upload/playing/page/2019/04/13/190413-17482-3-114.jpg',
                        title='Ctrl+F Brunch & Cafe',
                        text='泰式打拋雞肉三明治可頌',
                        actions=[
                            URITemplateAction(
                                label='推薦餐廳',
                                uri='https://ifoodie.tw/restaurant/59f375772756dd26326731c3-Ctrl-F-Brunch-Cafe'
                            ),

                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


if __name__ == '__main__':
    app.run()
