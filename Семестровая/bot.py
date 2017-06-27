import requests
import urllib.parse
import string


class ScriptParser:
    script_data = []
    
    user_data = {}
    
    def __init__(self):
        f = open('script.txt', 'r')
        for line in f:
            self.script_data.append(line)
    
    def reset(self,user_id):
        self.user_data[user_id] = {
            'vars' : [],
            'position' : '1'
        }
        
    def get_message_index(self, m_id):
        m_id = str(m_id)
        for i,line in enumerate(self.script_data):
            if line[:9] == ':MESSAGE ':
                #print('id:',i,line[:-1], '|', line[9:-1])
                if line[9:-1] == m_id:
                    return i
        
    def get_message_text(self, user_id):
        pos = self.user_data[user_id]['position']
        index = self.get_message_index(pos)
        out = ""
        variants = ""
        variants_mode = False
        theend = ""
        goodend = ""
        while True:
            cmd = False
            line = self.script_data[index]
            if line[0] == ':':
                cmd = True
                if line[:9] == ':MESSAGE ':
                    self.user_data[user_id]['position'] = line[9:-1]
                if line[:6] == ':GOTO ':
                    index = self.get_message_index(line[6:-1])
                    self.user_data[user_id]['position'] = line[6:-1]
                    continue
                if line[:9] == ':VARIANT ':
                    variants_mode = True
                    variants += line[9:].strip()+") "
                if line[:7] == ':VGOTO ':
                    variants_mode = False
                if line[:8] == ':SETVAR ':
                    self.user_data[user_id]['vars'].append(line[8:-1])
                if line[:8] == ':IFGOTO ':
                    param = line[8:-1].split(' ')
                    if self.user_data[user_id]['vars'].count(param[0]) > 0 :
                        index = self.get_message_index(param[1])
                        self.user_data[user_id]['position'] = param[1]
                        continue
                if line[:7] == ':BADEND':
                    theend = "(Плохой конец)\nВведите reset чтобы попробовать ещё раз."
                    break
                    
                if line[:8] == ':GOODEND':
                    theend = "(Конец)\nЕсли хотите попробовать ещё раз, напишите reset"
                    break
                    
                if line[:12] == ':END MESSAGE':
                    break
            else:
                if (line.strip() == '') and (cmd):
                    index += 1
                    continue
                if variants_mode:
                    variants += line
                else:                
                    out += line
            index += 1
        out+= "****\n"+variants+"\n"+theend
        return out
        
    def select_variant(self, user_id, variant_num):
        try:
            variant_num = int(variant_num)
        except ValueError:
            return False
    
        pos = self.user_data[user_id]['position']
        index = self.get_message_index(pos)
        variants_mode = False
        while True:
            line = self.script_data[index]
            if line[0] == ':':
                if line[:9] == ':VARIANT ':
                    if line[9:-1] == str(variant_num):
                        variants_mode = True
                if line[:7] == ':VGOTO ':
                    if variants_mode:
                        self.user_data[user_id]['position'] = line[7:-1]
                        return True
                if line[:12] == ':END MESSAGE':
                    return False
                    break
            index += 1
            
    def has_user(self, user_id):
        if self.user_data.get(user_id, False) == False:
            return False
        else:
            return True

class Bot:
    secretkey = 'somesecretkeyfjdsbfk903246738shfjscfcqyk'
    bot_token = '9fcf3360352115d935874b8a42aa570777c8fcd4a52fd8a5bceb53fbb594514154f4a5a5688d00988e0d1'
    script = None
    def __init__(self):
        self.script = ScriptParser()
    
    #Отправка запроса к vk Api
    def sendRequest(self, method ,data_array):
        request = {
            'access_token': self.bot_token,
            'v' : '5.25'
        }
        request.update(data_array)
        query = urllib.parse.urlencode(request)
        url = "https://api.vk.com/method/"+method
        #print('url:',url)
        return requests.post(url, data=query)
        
        
    #Пометка о том что сообщение прочитано
    def markAsReaded(self, message_id):
        return self.sendRequest('messages.markAsRead',{'message_ids' : message_id})

    #Отправка сообщения пользователю
    def sendMessage(self, user_id, message):
        r = {
            'user_id' : user_id,
            'message' : message,
        }
        return self.sendRequest('messages.send',r);

    #Обработка запроса от VK
    def request(self, req):
        #Подтверждение сервера
        if req['type'] == 'confirmation':
            response = input("Введите　код　подтверждения:")
            return response
        
        #Проверка сообщение пришло от vk или нет
        if req['secret'] != self.secretkey:
            return 'error'        

        #Сообщение от пользователя
        if req['type'] == 'message_new':
            #Отмечаем сообщение как прочитанное
            print('result',self.markAsReaded(req['object']['id']))
            #Разбор команд            
            cmd = req['object']['body']
            user_id = req['object']['user_id']
            
            if (cmd == 'reset') or (cmd == 'start') or (cmd == 'начать') or ( not self.script.has_user(user_id)):
                self.script.reset(user_id)
                msg = self.script.get_message_text(user_id)
                self.sendMessage(user_id,msg)
                return 'ok'
                
            if self.script.select_variant(user_id, cmd):
                msg = self.script.get_message_text(user_id)
                self.sendMessage(user_id,msg)
            else:
                self.sendMessage(user_id,"Нет такого варианта. Если хотите начать сначала, то напишите reset")
                    
            
        return "ok"
