<h2>Contact List</h2>
{% for contacts in contact %}
<li>{{ contacts.full_name: contacts.phone_number }}</li>
{% endfor %}