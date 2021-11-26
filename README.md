# AT-07_Python
26.11.2021
<p>Разница во времени выполнения filter.py и oldfilter.py связана со временем,</br> 
которое тратится на ввод данных</p>
<p>А filter_with_filename.py выполняется быстрее чем oldfilter.py, так как вместо</br> 
ручных циклов используются матричные преобразования такие как:</p>
<p><code>img_pixels[height: RightHeight, width: RightWidth] = \</br>
        [averageCol // Grey * Grey] * 3</code></p>
<p><code>averageCol = int(np.average(np.average(img_pixels[height: RightHeight, width: RightWidth])))</code></p>
<p><img src = "oldfilter.png"></p>
<p><img src = "filter.png"></p>
<p><img src = "filter_with_filename.png"></p>
<p><img src = "img2.jpg">
<p><img src = "res1.jpg">
<p><img src = "res2.jpg">
<p><img src = "res.jpg">
