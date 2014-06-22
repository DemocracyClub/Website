---
layout: default
---
<h2>{{ page.title }}</h2>
<p class="meta">{{ page.date | date_to_string }}</p>

<div class="post">
{{ content }}
</div>

<section>
    <hr>

{% capture text %}

### Comments

Rather than write a comment here, why not [join the mailing list](https://groups.google.com/forum/#!forum/democracy-club) tweet us [@democlub](https://twitter.com/democlub) or use the hashtag [#DemocracyClub](https://twitter.com/search?q=%23democracyclub)
{% endcapture %}

{{ text | markdownify }}

</section>