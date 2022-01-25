# **中國文化大學 畢業專題介紹**
利用機台上的鏡頭識別棋盤data，引導data傳回程式演算法電腦判斷下一步，再將結果傳至機械手臂配合鏡頭做出預期動作。  
Client: Google Colab，Python，OpenCV，Dobot  
Hardware:鏡頭＊1，機械手臂＊2，棋盤＊1，電腦＊1  
Panelists:[吳勁緯](https://github.com/wendellgithub0206 "link")，[蔣善澤]( https://github.com/temonmsl "link")  
guiding mentor:[林世崧](https://github.com/pccusslin0629 "link")
## AI下棋機器人之研製
主要分為三部分以及最終整合
* [棋藝演算法](https://github.com/wendellgithub0206/PGP/tree/main/%E6%A3%8B%E8%97%9D%E6%BC%94%E7%AE%97%E6%B3%95 "link")
* [影像處理](https://github.com/wendellgithub0206/PGP/tree/main/%E5%BD%B1%E5%83%8F%E8%99%95%E7%90%86 "link")
* [機械手臂](https://github.com/wendellgithub0206/PGP/tree/main/%E6%A9%9F%E6%A2%B0%E6%89%8B%E8%87%82%E6%8E%A7%E5%88%B6 "link")
## 棋藝演算法
**主要使用以下演算法**  
* 蒙地卡羅樹搜尋（MCTS）
評估：
	取得策略以及局是價值，策略用來計算出PUCT中棋步的機率分布，而局是價值則慧用來更新PUCT中的累計價值。
擴充：
  每試驗1次就進行擴充，因為本實驗配合神經網路已預測出棋步會下在哪了。
更新：
	取得局勢價值與試驗次數後，在返回跟節點途中，根據該價值進行節點資訊(累計價值及試驗次數)的更新。
## 影像處理
四子棋適用於6*7的棋盤，而實際影像中框出的影像為640*480而格式為15*15棋盤，只要做3步驟就能辨識並且將任意自訂棋盤從圖片分割出來，第一步先根據棋盤顏色設定顏色的上限與下限並且利用掩模(mask)屏蔽不屬於此顏色上下限範圍的區域，第二步覆蓋屬於此顏色上下限範圍卻不是我們所需要的區域，第三步畫出輪廓確認此區域是否為我們所需要的正確區域在並且擷取出來。
## 機械手臂
使用Dobot Magician提供的DobotVisionStudio開發套件能簡單的實做機器人運動之控制。

