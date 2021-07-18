# MPU 9250數據擷取

[雲端資料夾](https://drive.google.com/drive/folders/1gK3bhSXd41HmCHAkCUYq4XbA05TIExSr)

[線上共筆](https://hackmd.io/hz33vW3CT6ewpjIzsDVQ-A?both)

---

# 馬達資料標準檔名規範
ex:`1100713_N_S25_L50_HZ500`
* 1100713：日期
* N：狀態，總共有四種(N=>正常馬達、RU=>轉子不平衡、RB=>轉子斷條、SS=>定子短路)
* S25：速度與運轉功率=>S：speed，25：運轉%數(0,25,75,100)
* L50：附載(0,25,50,75,100,125)
* HZ500：Sample rate

---

# ESP32 使用方式
**加速度資料** -> 短路 `Pin17`  & `Pin16`

**角速度資料** -> 開路 `Pin17`  & `Pin16`

[腳位圖](https://i.imgur.com/agXB1Zo.png)
