---
title: "Default of Credit Cards"
output:
  html_document:
    toc: yes
    keep_md: yes
  pdf_document:
    toc: yes
always_allow_html: yes
---



## Data 

- https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset 

## Preprocessing 

- BP_R*
- CB_*

## EDA

#### Target class distributions 



<table class="table" style="margin-left: auto; margin-right: auto;">
<caption>Table 1. Target Class Distribution in Training Set</caption>
 <thead>
  <tr>
   <th style="text-align:right;"> class </th>
   <th style="text-align:right;"> count </th>
   <th style="text-align:right;"> percent </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 18668 </td>
   <td style="text-align:right;"> 77.8 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 5332 </td>
   <td style="text-align:right;"> 22.2 </td>
  </tr>
</tbody>
</table>

<table class="table" style="margin-left: auto; margin-right: auto;">
<caption>Table 2. Target Class Distribution in Test Set</caption>
 <thead>
  <tr>
   <th style="text-align:right;"> class </th>
   <th style="text-align:right;"> count </th>
   <th style="text-align:right;"> percent </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 4696 </td>
   <td style="text-align:right;"> 78.3 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 1304 </td>
   <td style="text-align:right;"> 21.7 </td>
  </tr>
</tbody>
</table>
