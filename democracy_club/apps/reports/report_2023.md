{% load static %}---
hero_image: {% static "images/maze_illustration_no_text.png" %}
---


# Local elections 4 and 18 May&nbsp;2023

## Highlights
* More than two million postcode searches from the UK public.
* Major new collaboration with BBC News.
* Updated our systems to accommodate the 2022 Elections Act.
* Implemented significant changes to Who Can I Vote For.
* Collected polling station data from every participating council.
* 26,570 candidates added to the database.
* Integrated data from a new electoral software supplier into the polling 
  station finder.

## Election Overview
In May 2023, [elections were held to 230 English councils and all councils in Northern Ireland](https://democracyclub.org.uk/blog/2023/03/02/whats-up-for-election-in-2023/). England went to the polls on 4 May, while Northern Ireland voted on 18 May, its elections postponed as a consequence of the King’s coronation on 6 May. 

These were the first elections to take place under the provisions of the 2022 Elections Act, which changed electoral systems for a number of posts and introduced a requirement for voters to display identification at polling stations for all non-devolved elections. Democracy Club worked hard to ensure that the new electoral laws were reflected in our systems, and our elections database is now able to automatically apply the correct voter ID requirements and voting system to each election type.

Our data collection went as planned. For the second year running we obtained polling station data from every council holding elections. Our amazing volunteers answered the call once again, ensuring we had a full database of candidates within a week of nominations closing.

The most notable success of the election was a new collaboration with the BBC, which used our data to power a postcode lookup on its news website. The Corporation praised the quality of our data, and we hope to work with them again next year. This was in partnership with the Electoral Commission, [with whom we continue to work closely](https://www.electoralcommission.org.uk/all-information-you-need-about-elections-4-may).

Our work was rewarded with more than two million postcode searches from the UK public during the two election weeks. Enormous thanks to everyone who volunteered their time over the election period, and to elections teams in England and Northern Ireland - we couldn’t do it without you!

> “This website was great, very helpful to try and understand candidates”

> “Gave me greater clarity on who to vote for and who not. Thanks”

> “Easy, quick info, useful”

> “This is really helpful, thank you for compiling it all.”

> “I was feeling apathetic and not going to vote now I feel I’ve got to make the effort”

<figure>
<img src="{% static 'report_2023/images/bbc-widget.png' %}" alt="BBC Northern Ireland election lookup">
<figcaption>
  BBC Northern Ireland election lookup
</figcaption>
</figure>

## Data Collection

### Polling Stations
Once again we’re delighted to report that we received polling station data from 100% of English councils, plus the Electoral Office for Northern Ireland. We can now say that every single UK council area has supplied us with polling station data for at least one election since 2019. This is a massive organisational milestone, putting us in a good position to reach 100% coverage for the next general election. The communications work continues to become smoother, with a majority of this year’s councils using [our self-serve uploader](https://wheredoivote.co.uk/uploads/about/), which was introduced last year. 

Special thanks are due to the Electoral Commission and the Association of Electoral Administrators, who went out of their way to ensure that every council was able to provide us with polling station data.

One development in this area was the launch last year of a new Electoral Management Software (EMS), FCS Elections. After consulting with us, FCS provided an Application Programming Interface (API) which allows us to plug directly into a council’s polling station database, removing the need for the council to generate and email a file export. This is an exciting development, allowing us to publish polling station data faster and with greater accuracy than previously. It also opens up the possibility of drawing more information from councils, including candidate data. We’re actively investigating this ahead of the 2024 elections, and look forward to working more with FCS and their customers over the coming years.

### Candidates
This year saw more councillors up for election than at any time since 2019: [8,519 seats](https://democracyclub.org.uk/blog/2023/03/02/whats-up-for-election-in-2023/) and [26,570 candidates](https://democracyclub.org.uk/blog/2023/04/11/2023-local-election-data-summary/). Thanks to an excellent volunteer effort, the 25,700 candidates for the English local elections were collected and published within a week of publication.

Our Northern Ireland candidate collection presented a different though no less encouraging picture. In the weeks prior to SoPN day, volunteers sourced hundreds of candidates from political party announcements, meaning that the vast majority of candidates were already in the system before nominations closed. This meant that, although nomination day itself saw lower volunteer engagement similar to [last year’s Scottish SoPN day](https://democracyclub.org.uk/report_2022/#candidates), the amount of data collection needed was much lower, and this combined with the relatively small number of candidates overall meant that we were able to complete the collection the day after nominations closed.

We are experiencing increasing difficulties with our archive of candidate contact details and especially election statements. We currently have no way of easily identifying outdated information, meaning that many candidate profiles are now largely out of date. We want to [look into this issue](https://github.com/DemocracyClub/yournextrepresentative/issues/2129) in time for the 2024 elections.

Changes to Twitter’s free API  access sadly meant that we have had to retire TwitterBot, which auto-updated twitter handles and verified accounts existed, after 15,767 edits. This will mean that our archive of Twitter accounts will begin to degrade. We’ve also had to remove the Twitter feed preview integration from candidate profiles on WhoCanIVoteFor, as changes to who can view Tweets mean that these no longer work. It remains to be seen which social media platform will emerge as the most popular among politicians and candidates should Twitter continue on this path; in the meantime we are working to add a greater selection to candidate profiles, including Threads, Bluesky, and Mastodon. In any case, given our tight margins, sponsorship for these types of unforeseen costs would be useful to ensure continuity of our candidate data.

### Election Results

Thanks again to our volunteers, all votes cast in the English local elections were collected by the middle of May. Before the election we hoped to be able to [improve our election results CSV](https://candidates.democracyclub.org.uk/uk_results/) to include uncontested seats and additional geographic data, but unfortunately due to limited funding and organisational capacity given the increased usage, we were not able to bring this about in time. However, we were able to identify gaps in some of our automated results collection methods, and will be investigating these ahead of the next local elections (specifically, how to better automate collection of turnout).

###Volunteers and the Club

During March, April, and May, more than 1,500 new user accounts were created on [our candidate database](https://candidates.democracyclub.org.uk/), bringing the total to 14,000. Users made over 83,500 edits to the database over the same three months; eighteen users made more than 1,000 edits each. At time of writing, our Slack Channel contains over 1,000 members.

## Evaluating overall reach and impact
### Usage statistics
Combining the two election weeks (1-4 May and 15-18 May), we processed [over two million postcode searches](https://democracyclub.org.uk/blog/2023/05/23/2023-postcode-search-summary/). Of these, 1,362,656 were received from council areas holding elections that week. These numbers are very similar to our 2021 and 2022 figures, despite the fact that far fewer people were able to vote in 2023. Compared with 2019 (the last time these elections occurred) postcode searches have more than doubled.

<figure>
<img src="{% static 'report_2023/images/searches.png' %}" alt="Postcode 
searches per election week (Monday—Thursday)">
<figcaption>
  Postcode searches per election week (Monday-Thursday)
</figcaption>
</figure>

One reason for these strong numbers was the involvement of the BBC, who used our data (via the Electoral Commission) to power lookups on the BBC news website for both England and Northern Ireland, netting us 426,000 searches. This more than made up for the loss of InYourArea, which did not use the data this year for technical reasons. We also received 200,000 searches from a tactical voting website which used our API.

<table class="ds-table">
<caption>API traffic, 1-5 and 15-18 May, 2023</caption>

<tr>
    <th>User</th>
    <th>Searches (both weeks)</th>
</tr>

<tr>
    <td>WhoCanIVoteFor</td>
    <td>487,959</td>
</tr>
<tr>
    <td>Electoral Commission</td>
    <td>425,116</td>
</tr>
<tr>
<td>BBC News</td>
<td>425,498</td>
</tr>
<tr><td>WhereDoIVote</td>
<td>303,453</td>
<tr>
<td>StopTheTories.vote</td>
<td>245,061</td>
</tr>
<tr>
<td>Gov.uk ERO finder</td>
<td>54,476</td>
</tr>

 </table>
Changes to Google Analytics led to us dropping the service earlier this year. We’re exploring alternatives for analysing user traffic on WhoCanIVoteFor and WhereDoIVote. Consequently we are unable to provide visitor figures for this year.

We continue to find great examples of political parties using our services, especially WhereDoIVote, and [blogged about it earlier in the year](https://democracyclub.org.uk/blog/2023/02/17/why-democracy-club-is-non-partisan/) (since publishing the blog, Reform UK have confirmed to us that they use WhoCanIVoteFor a lot internally).

<figure>
<img src="{% static 'report_2023/images/voter_id.png' %}" alt="WhereDoIVote.co.
uk advertised on a leaflet">
<figcaption>
  WhereDoIVote.co.uk advertised on a leaflet from a political party delivered to addresses in Bath & North East Somerset on polling day.
</figcaption>
</figure>


### Council partnerships
Of the 230 English councils holding elections this year, 67 (29%) embedded 
the Electoral Commission's or [Democracy Club’s widget](https://democracyclub.org.uk/projects/polling-stations/embed/) on their own websites, collectively receiving 73,000 postcode searches for the week 1-4 May. The top user was East Devon council, who netted 6,000 searches by including the EC widget in a header which followed the user around their website until dismissed.


<figure>
<img src="{% static 'report_2023/images/east-devon.png' %}" 
alt="East Devon Council’s front page on election day">
<figcaption>
  East Devon Council’s front page on election day, with embedded Electoral Commission Widget.
</figcaption>
</figure>

Use of the widget also reflects a growing interest in our candidate information on the part of councils. One third of council widget users chose to use the [tools which also displayed candidate information](https://democracyclub.org.uk/projects/election-widget/), accounting for 43% of the searches received from council widgets. A handful of councils asked whether they could provide candidate lists to us, something we cannot yet support without additional staff capacity. One council got in touch with us to request support for more political party colours on the widget, with which we were happy to comply.

More than simply providing us with data, many councils feature our services as a core part of their election communications. For example, this year one large city council dropped their in-house finder in favour of ours, saving money and resources. 

We plan to build on these relationships as we head towards the next general election. We’re reaching out to councils and EMS suppliers to explore how we might improve the range of information we can display on the finder, including accessibility information and candidate lists. We also want to expand our coverage of by-elections to establish the finder as a fully comprehensive service.

<figure>
<img src="{% static 'report_2023/images/manchester.png' %}" 
alt="Link to WhereDoIVote.co.uk on Manchester Council’s website. 
">
<figcaption>
Link to WhereDoIVote.co.uk on Manchester Council’s website. 
</figcaption>
</figure>

### API and data service issues
This year our services experienced some instability and downtime. On the morning of 4 May, problems related to a bad system configuration caused a number of users to see the message ‘this postcode is not recognised’, despite entering a correct postcode. We estimate that this affected around 25,000 postcode searches during the morning. Later in the day, our polling station database was down for around 20 minutes due to a human error introduced when cancelling a countermanded poll. Unlike the previous issue, this did not affect election or candidate information. On 18 May, another error caused polling stations to go down during the morning, although once again elections and candidates were unaffected.

Although we do not think these issues had a serious impact on our overall delivery of the election (at least, our user and customer feedback does not suggest this), we are taking this extremely seriously and will be putting measures in place to ensure that these mistakes cannot occur in the future.

### User feedback
Each year we ask visitors to our sites the question: ‘Did you find what you were looking for?’. 

Of the 1,690 users of WhereDoIVote who answered between 1 and 4 May, 92% said yes. This is a small drop as compared to last year - possibly due to the service issues as described above - but is within the usual 90%+ range which the site receives.

Of the 2,141 replies on WhoCanIVoteFor between 1 and 4 May, 64% answered yes. This is a drop of 5% compared with last year, and the first election which has recorded a fall. 

<figure>
<img src="{% static 'report_2023/images/satisfaction.png' %}" 
alt="Graph showing user satisfaction. 
">
<figcaption>
‘Did you find what you were looking for?’ - % answering ‘yes’ during each election.
</figcaption>
</figure>


Once again we also asked users whether the information had made them more likely to vote. Of the 1,417 users of WhereDoIVote who answered the question, 76% said yes, a drop from the 83% reported last year. On WhoCanIVoteFor 46% said yes, a [drop from 52% last year](https://democracyclub.org.uk/report_2022/#user-feedback). As we explained then, negative answers to this question do not imply that the user is less likely to vote.

>“I always exercise my right to vote in elections thus Q2 above has no relevance to me”

We’ll aim to add a third ‘I always vote’ answer to this question before the next election!

### Press and PR
Public communications took a bit of a back seat for us this year for positive reasons: we were too busy! Regardless, a number of media organisations linked to WhoCanIVoteFor or WhereDoIVote as part of their election coverage. Our elections data was also used in the following:

* National World used our candidate data to identify candidates who were 
[standing for more than one seat](https://www.nationalworld.com/news/politics/local-elections-2023-candidates-standing-multiple-seats-liberal-democrat-conservatives-4125327).
* The Electoral Reform Society produced a [press release on uncontested and 
  under contested seats](https://www.electoral-reform.org.uk/elections-cancelled-90000-denied-any-say-in-local-elections/), again using our candidate data.
* The Institute for Government published [a great explainer using our data on 
  the number of seats up for election](https://www.instituteforgovernment.org.uk/explainer/local-elections-2023).

* With ongoing drama at Twitter (as well as the fact that we deleted our Facebook account last year due to low engagement), Democracy Club now has a Mastodon account. [Give us a follow](https://mastodon.me.uk/@DemocracyClub)!

## Technical developments
### Every Election
Much of late 2022 and early 2023 was occupied with modifying our systems to take account of the [2022 Elections Act](https://www.legislation.gov.uk/ukpga/2022/37/contents/enacted). Our systems are now able to automatically identify which elections require voter ID and which do not. We’re also able to change the voting system assigned to s specific election type, something which our previous static model was unable to do. This means we can now support any [Welsh councils which choose to switch to the Single Transferable Vote](https://www.legislation.gov.uk/asc/2021/1/part/1/crossheading/voting-systems-for-elections-to-principal-councils/enacted).

This work was bundled together with an upgrade to Every Election, which now [sports our modern design system and maps](https://democracyclub.org.uk/blog/2023/01/26/welcome-to-the-new-look-every-election/). We also made the first step towards grasping the nettle of Electoral Change Orders; these modify the boundaries of council wards, but due to the way they are published and enacted they often prevent us from creating the May elections [earlier than we would like](https://democracyclub.org.uk/blog/2017/02/23/ordnance-survey-are-getting-way-open-election-data/). 

Shortly after the local elections, we were asked by the Electoral Commission and South Lanarkshire Council to modify our API to allow for the publishing of information relating to the [Rutherglen and Hamilton West recall petition](https://democracyclub.org.uk/blog/2023/06/16/recall-petitions/), work which is now published on the website of the Electoral Commission. 

### WhoCanIVoteFor.co.uk
The biggest development is that WCIVF can now handle split postcodes - that is, when two wards have properties that share a postcode. Previously we would show the ballots for the weighted centre of the postcode, but now we offer users of WCIVF an address picker, in line with our other products. Sym has previously written [about split postcodes](https://democracyclub.org.uk/blog/2017/03/20/4314-times-when-postcodes-arent-good-enough/) on our blog.

At a technical level, this work was done by getting WhoCanIVoteFor to consume our main developers API, rather than trying to perform its own mapping between postcodes and elections. One of the main advantages of the API is that it always resolves down to addresses if needs be. This has also allowed us to simplify our election day traffic scaling operations on the site: the API gets most of the traffic and WhoCanIVoteFor only needs to perform very simple queries on essentially static data.  

Meanwhile we’ve also [redesigned the political party pages](https://whocanivotefor.co.uk/parties/). This is something we’ve been itching to do for years; before now, the political party pages consisted of nothing more than an extremely long list of every ward/constituency the party has fielded candidates in, shorn of any additional context. This has now been replaced with a summary of (and a link to) the relevant page in the Electoral Commission’s database of political parties. This gives voters more information about how the party might appear on their ballot paper, and also acts as an easier point of access to the Commission’s database.
### Candidates database
We made a range of improvements to our candidates database, including to the photo moderation and crowdsourcing interface. Notably, we introduced a new vandalism prevention process, with name changes on ‘locked’ ballots now requiring review before they are published.
## Organisational developments
### Board and core team
Since our last election report was published, Democracy Club has seen [a significant amount of organisational change](https://democracyclub.org.uk/blog/2022/09/07/all-change/). Two board members left and three new members joined, with Mevan Babakar taking over from Alice Casey as Chair.

In terms of the core team, we hired a new full-time developer, Bek Lewis, who is focusing on improving WhoCanIVoteFor. Due to the relatively small scale of the election (in terms of councils involved), and the leaps we’ve made in terms of automating the polling station data collection process, we decided not to hire an elections assistant this year.

As part of our organisational development we also hired a CEO, Shabira Papain, who was with us from September until March.

The board have been pleased to have Shabira's support over a time of transition for Democracy Club, she has been instrumental in helping us secure key insights that will help the CIC to progress. Having achieved some clarity as to what the organisation will need for the coming years, she stepped down to turn her attention back toward working with and improving direct engagement of underrepresented communities. We wish her all the best on this vital mission.

We are very grateful to Shabira for taking on the role of CEO at Democracy Club, and would like to formally extend our thanks to her for the time spent with us. 

## Thank you!
Democracy Club can only do what it does thanks to the hard work of hundreds of volunteers and electoral administrators. To everyone who lent a hand this year, and continue to maintain our databases: thank you. UK democracy is stronger and healthier for your work.
