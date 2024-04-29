Ruler Code: 

<head>
    <style>
     .ruler {
        position: absolute;
        bottom: 165.8px;  /* adjust this value to move the ruler up or down */
        left: 0;
        width: 100%;
        height: 20px; /* adjust this value to change the height of the ruler */
        background-color: red;
        border-bottom: 1px solid lime;
      }
      
     .ruler-unit {
        float: left;
        width: 20px; /* adjust this value to change the width of each unit */
        height: 20px;
        text-align: center;
        font-size: 12px;
        margin-right: 10px;
      }
      
     .ruler-unit:before {
        content: "";
        display: block;
        width: 1px;
        height: 10px;
        background-color: #666;
        margin: 0 auto;
      }
    </style>
  </head>
  <body>
    <div class="ruler">
      <div class="ruler-unit">0</div>
      <div class="ruler-unit">1</div>
      <div class="ruler-unit">2</div>
      <div class="ruler-unit">3</div>
      <div class="ruler-unit">4</div>
      <div class="ruler-unit">5</div>
      <div class="ruler-unit">6</div>
      <div class="ruler-unit">7</div>
      <div class="ruler-unit">8</div>
      <div class="ruler-unit">9</div>
      <div class="ruler-unit">10</div>
      <div class="ruler-unit">11</div>
    </div>
  </body>