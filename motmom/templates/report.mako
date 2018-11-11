# -*- coding: utf-8 -*-
<%inherit file="admin_layout.mako"/>

<%block name="page_title">
  Отчет
</%block>

<h2>Сводный отчет по сотрудникам</h2>
<form action="${request.route_url('report')}" method="post">
<div class="form-group">
  <label for="from_date">from:</label>
  <input type="date" maxlength="100" name="from_date" minlength="6" value="${from_date}" required>
</div>
<div class="form-group">
    <label for="to_date">to:</label>
    <input type="date" maxlength="20" name="to_date" minlength="6" value="${to_date}" required>
</div>

  <input type="submit" name="form.submitted" value="Filter" class="button">

</form>
<br><br>
<ul class="list-group home_list">
% if records:
  % for record in records:
  <li class="list-group-item">
    <span class="name">${record['username']}: </span>
    <span class="name">${record['total']} руб.</span>


  </li>
  % endfor
% else:
  <li>There are no records this period</li>
% endif

</ul>




