# -*- coding: utf-8 -*-
<%inherit file="admin_layout.mako"/>

<%block name="page_title">
  Заказы
</%block>

<h2>Список всех заказов</h2>

<table class="table bidlist">
  <thead>
    <tr>
      <th scope="col">№</th>
      <th scope="col">Сотрудник</th>
      <th scope="col">Заказ</th>
      <th scope="col">Сумма</th>
      <th scope="col">Комментарий</th>
      <th scope="col">Дата</th>
      <th scope="col">Удалить</th>
    </tr>
  </thead>
  <tbody>
% if orders:
  % for order in orders:
  <tr>
    <th scope="row">${order.id}</th>
    <td >${order.creator.name}</td>
    <td >${order.data}</td>
    <td>${order.price} руб.</td>
    <td >${order.comment}</td>
    <td >${order.datetime}</td>
    <td><a href="${request.route_url('delete_order', id=order.id)}">Удалить</a></td>
  </tr>
  % endfor
    </tbody>
  </table>
% else:
  <li>There are no orders</li>
% endif
