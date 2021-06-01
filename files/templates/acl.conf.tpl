acl num 2001
{% for host in allow_ip %}
rule 5 permit source {{ host }}
{% endfor %}
{% for host in disallow_ip %}
rule 10 deny source {{ host }}
{% endfor %}
interface {{ interface }}
traffic-fil inbo acl 2001