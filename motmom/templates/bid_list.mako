# -*- coding: utf-8 -*-
<%inherit file="layout.mako"/>

<%block name="page_title">
    Мои заказы
</%block>

<h2>Список моих заказов</h2>

<table class="table bidlist">
  <thead>
    <tr>
      <th scope="col">№</th>
      <th scope="col">Заказ</th>
      <th scope="col">Сумма</th>
      <th scope="col">qr код</th>
      <th scope="col">Комментарий</th>
      <th scope="col">Дата</th>
    </tr>
  </thead>
  <tbody>
% if bids:
  % for bid in bids:
  <tr>
    <th scope="row">${bid.id}</th>
    <td >${bid.data}</td>
    <td>${bid.price} руб.</td>
    <td><img src = "${bid.qrcode}"></td>
    <td>${bid.comment}</td>
    <td>${bid.datetime}</td>
  </tr>
  % endfor
    </tbody>
  </table>
% else:
  <li>There are no bids</li>
% endif











