# **中國文化大學 畢業專題介紹**
利用機台上的鏡頭識別棋盤data，引導data傳回程式演算法電腦判斷下一步，再將結果傳至機械手臂配合鏡頭做出預期動作。  
Client: Google Colab，Python，OpenCV，Dobot  
Hardware:鏡頭＊1，機械手臂＊2，棋盤＊1，電腦＊1  
Panelists:[吳勁緯](https://github.com/wendellgithub0206 "link")，[蔣善澤]( https://github.com/temonmsl "link")  
guiding mentor:[林世崧](https://github.com/pccusslin0629 "link")
## AI下棋機器人之研製
主要分為三部分以及最終整合
* [棋藝主程式]<br/>
  [四子棋](https://github.com/wendellgithub0206/PGP/tree/main/%E5%9B%9B%E5%AD%90%E6%A3%8B "link")
  [五子棋](https://github.com/wendellgithub0206/PGP/tree/main/%E4%BA%94%E5%AD%90%E6%A3%8B "link")
* [影像處理](https://github.com/wendellgithub0206/PGP/tree/main/%E5%BD%B1%E5%83%8F%E8%99%95%E7%90%86 "link")
* [機械手臂](https://github.com/wendellgithub0206/PGP/tree/main/%E6%A9%9F%E6%A2%B0%E6%89%8B%E8%87%82 "link")
## AI

* 強化式學習<br/>
以大量資料為基礎的監督式學習非監督式學習不同，期目的是為了在特定環境中採取適當的動作。比如自動駕駛就是強化式學習的應用。 
強化式學習(Reinforcement learning)是透過代理人(agent)根據環境狀態(environment)採取動作(action)已獲得更多回饋值(reward)的方法，此法與監督非監督式學習不同，在於不依靠訓練資料，只靠代理人本身已試誤法來進行學習。<br/>
![image](https://github.com/wendellgithub0206/PGP/blob/main/%E5%BC%B7%E5%8C%96%E5%BC%8F%E5%AD%B8%E7%BF%92.png)
* 殘差網路(ResNet) <br/>
在神經網路中我們可以透過加深層數來提取更複雜的特徵，但是當神經網路的深度達到某個程度時，訓練資料的準確率會上升然後達到飽和，然後迅速下降，就是光訓練資料的成效就很差。 
殘差網路第一次出現是在2015年的ImageNet影像辨識競賽，已超高準確率獲得當年冠軍。殘差網路就是使用了152層網路結構，超過百層的殘差網路卻不會降低準確率的關鍵在於其特殊的殘差塊(Residual block)結構，設計一條捷徑來讓淺層的網路也能得到較有效果的訓練使得在深度較深的模型在做反向傳播時不會因傳遞太多層而導致梯度嚴重下降，使得我們訓練更深層的神經網路，獲得更好的成果。
![image](https://github.com/wendellgithub0206/PGP/blob/main/%E6%AE%98%E5%B7%AE%E7%B6%B2%E8%B7%AF.png)

## 棋藝演算法
**主要使用以下演算法**  
* 蒙地卡羅樹搜尋（MCTS）<br/>
評估：<br/>
	取得策略以及局是價值，策略用來計算出PUCT中棋步的機率分布，而局是價值則慧用來更新PUCT中的累計價值。<br/>
擴充：<br/>
  	每試驗1次就進行擴充，因為本實驗配合神經網路已預測出棋步會下在哪了。<br/>
更新：<br/>
	取得局勢價值與試驗次數後，在返回跟節點途中，根據該價值進行節點資訊(累計價值及試驗次數)的更新。<br/>
## 影像處理
四子棋適用於6*7的棋盤，而實際影像中框出的影像為640*480而格式為15*15棋盤，只要做3步驟就能辨識並且將任意自訂棋盤從圖片分割出來，第一步先根據棋盤顏色設定顏色的上限與下限並且利用掩模(mask)屏蔽不屬於此顏色上下限範圍的區域，第二步覆蓋屬於此顏色上下限範圍卻不是我們所需要的區域，第三步畫出輪廓確認此區域是否為我們所需要的正確區域在並且擷取出來。
## 機械手臂
使用Dobot Magician提供的DobotVisionStudio開發套件能簡單的實做機器人運動之控制。
## Google Colab
Google Colab是一個基於 Jupyter Notebook 的免費CPU虛擬機，透過瀏覽器即可編寫程式，當離開瀏覽器操作畫面，虛擬機上的操作資料都被清空，所以使用者不需要擔心操作不慎搞壞機器。除了資料存至雲端虛擬機上之外，還可以連接Google Drive雲端硬碟，將訓練完成的AI模型或資料科學處理的資料進行儲存，而Google Colab擁有以下幾個特點：<br/>
1不需任何設定：瀏覽器開起Google Colab，連線完成即建立玩虛擬機，就可以使用Google Colab的功能。<br>
2免費使用 GPU或TPU：Colab中可選用的GPU通常包括Nvidia K80，T4，P4和P100，但使用者不能選擇使用哪種類型的GPU，由於免費使用的關係，Colab無法保證資源，會依據時間和使用者有浮動，筆記本最長可執行	12小時；如果一定需要使用GPU，可以選擇升級為付費版本Colab Pro，每月支付9美金，優先存取更快速的 GPU 和 TPU。<br>
3共用功能：Colab筆記本是存在Google Drive，方便管理ipynb檔案，也可以將程式檔案ipynb下載分享給其他人使用。<br>
4開啟GitHub筆記本：透過開啟筆記本功能，可以點選GitHub選項，貼上你從GitHub看到的ipynb檔案網址，就可以在Google Colab開啟檔案或複製至自身的Google Drive。<br>
