//https://blog.csdn.net/Naisu_kun/article/details/107164844
#include <WiFi.h>
#include <ESPAsyncWebServer.h> //引入相应库


const char *ssid = "Yyuying90";
const char *password = "25243166";


AsyncWebServer server(80); // 声明WebServer对象

AsyncWebSocket ws("/"); // WebSocket对象，url为/

// WebSocket事件回调函数
void onEventHandle(AsyncWebSocket *server, AsyncWebSocketClient *client, AwsEventType type, void *arg, uint8_t *data, size_t len)
{
  if (type == WS_EVT_CONNECT) // 有客户端建立连接
  {
    Serial.printf("ws[%s][%u] connect\n", server->url(), client->id());
    client->printf("Hello Client %u !", client->id()); // 向客户端发送数据
    client->ping();                                    // 向客户端发送ping
  }
  else if (type == WS_EVT_DISCONNECT) // 有客户端断开连接
  {
    Serial.printf("ws[%s][%u] disconnect: %u\n", server->url(), client->id());
  }
  else if (type == WS_EVT_ERROR) // 发生错误
  {
    Serial.printf("ws[%s][%u] error(%u): %s\n", server->url(), client->id(), *((uint16_t *)arg), (char *)data);
  }
  else if (type == WS_EVT_PONG) // 收到客户端对服务器发出的ping进行应答（pong消息）
  {
    Serial.printf("ws[%s][%u] pong[%u]: %s\n", server->url(), client->id(), len, (len) ? (char *)data : "");
  }
  else if (type == WS_EVT_DATA) // 收到来自客户端的数据
  {
    AwsFrameInfo *info = (AwsFrameInfo *)arg;
    Serial.printf("ws[%s][%u] frame[%u] %s[%llu - %llu]: ", server->url(), client->id(), info->num, (info->message_opcode == WS_TEXT) ? "text" : "binary", info->index, info->index + len);
    data[len] = 0;
    Serial.printf("%s\n", (char *)data);
  }
}

void setup()
{
  Serial.begin(115200);
  Serial.println();

  WiFi.mode(WIFI_STA);
  WiFi.setSleep(false);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected");
  Serial.print("IP Address:");
  Serial.println(WiFi.localIP());

  ws.onEvent(onEventHandle); // 绑定回调函数
  server.addHandler(&ws);    // 将WebSocket添加到服务器中

//  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) { //注册链接"/lambda"与对应回调函数（匿名函数形式声明）
//    request->send(200, "text/html", indexhtml);                 //向客户端发送响应和内容
//  });

  server.begin(); //启动服务器

  Serial.println("Web server started");
}

int i=0;
void loop()
{
  delay(50);
  if (i++>1000)
    i=0;
//  Serial.println(i);
  ws.textAll(String(i)); // 向所有建立连接的客户端发送数据
  ws.cleanupClients();     // 关闭过多的WebSocket连接以节省资源
}
