{% load static %}

# Where Do I Vote - User Feedback May 2018

## Introduction

Prior to the general election in June 2017, we introduced a feedback form on [wheredoivote.co.uk](https://wheredoivote.co.uk/) asking a Yes/No question: “Did you find this useful?” and a follow up text question “Can you tell us anything more?”. This survey yielded a lot of useful feedback and we've spent much of the last year making improvements inspired by that feedback. We have continued to collect user feedback around the local elections which took place in May 2018.

As in 2017, we only showed the feedback form in situations where we could provide the user with some information. We have implicitly assumed that in cases where we showed the “We don’t have data for your area” page and provided contact details for the user’s council, this was not helpful and didn’t ask for feedback. The way to fix/improve that is to have greater coverage. We also only showed users a feedback form on our own website - it wasn’t shown to embedded users and we don’t have any data about users consuming our data on third party websites via the API.

This year we slightly modified our question, adding an additional option for "Report a problem with this page". For the purposes of comparing to June 2017 results, we have implicitly assumed that users who reported a problem also did not find this helpful.

From midnight on Monday 30 May to close of polls on Thursday 3 May, we collected 1,711 responses. This gives a smaller evidence base to work with than in 2017 (a reflection of the lower level of website usage and interest in local elections). Of the 1,711 responses:

<div class="ds-table">
<table>
<tr>
<th>Found useful</th>
<th>Number</th>
<th>Percent</th>
</tr>
<tr>
<td>Yes</td>
<td>1,645</td>
<td>96.14%</td>
</tr>
<tr>
<td>No</td>
<td>66</td>
<td>3.86%</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>1,711</td>
<td>&nbsp;</td>
</tr>
</table>
</div>

This represents an improvement in the proportion of satisfied users from last year's baseline. It is probably realistic to attribute some of this increase to improvements we have made based on last year's feedback.

Additionally, we collected around 150 free-text comments. Given the low volume of comments, it is more difficult to identify strong themes than in 2017, but there are some insights to be gained.

## What are we doing well?

We received numerous positive comments about the site. The comments we received about the information we've chosen to present and prioritise were positive, confirming that moving to a more mobile-friendly single-column layout and the work we've done on design and information hierarchy is better meeting user needs:

> Really helpful to be able to know how far to walk from my property to the polling station so I can fit it in to my normal morning routine!

<!---->

> Precisely the information I was looking for.

<!---->

> Really helpful stuff, I also wanted to know what time it's open until and you told me that too.

<!---->

> A very useful page – came here to find out where my polling station is and happy to also find the Electoral Registration Officer details

Additionally, comments about design and UX were also positive, validating that the work we've done to produce concise accessible content has also been beneficial:

> Clear and easy to use.

<!---->

> I am disabled and registered visually impaired. This site was so so easy to use. All the information I need is right there.

<!---->

> Very informative. Quick and simple. Like the User interface and the map feature.

<!---->

> Simple google search. first hit. Information found in 30 secs. Many thanks


It is also worth noting that there were two topics which we identified as needing improvement after receiving a large volume of negative comments last year:

* Opening hours were not obvious enough
* Poor quality route/directions

These two issues were the most obvious themes in the negative user feedback in 2017 and we received no negative comments about these topics this May, indicating that the improvements we have made here have been successful.

## What should we improve?

### Bug Reports

The most common class of negative comments was feedback from users reporting problems or incorrect information:

> Map is incorrect. Postcode is incorrect. Church is the other end of Magdalen Way, at junction with Hertford Way

<!---->

> The polling station postcode is incorrect. It's listed as E2 8SB but it's actually at E2 8QY.

<!---->

> I went to this location to vote and it is not a polling station!!


In some ways this is the worst class of negative comment for us to receive, but also highly valuable as it allows us to track down problems and fix them. Over the course of the week we were able to follow up on the majority of issues reported and we made a number of corrections as a result of information provided by users.

Inspired by our [case study on GetToThePolls.com](https://democracyclub.org.uk/blog/2017/10/20/where-do-i-vote-tour/), we added a specific option for 'Report a problem with this page'. Most people reporting a problem did use the 'report a problem...' option and separating these reports from other negative feedback did help us to identify and respond to problems more quickly.

It is difficult to compare our results here to 2017 because we didn't explicitly record a number of issues reported. Also introducing this option to the form may have changed user reporting behaviour. In response to some of the issues identified last year, we introduced additional consistency checks to the import process which allowed us to identify more problems before deploying any data to the site. Anecdotally it did seem like there were fewer problems identified by users and the problems reported were of lower severity. This is something we will continue to monitor in April 2019.

### Additional Information

The other common request we received was for additional information about the elections. Users wanted to know which ward they are in:

> It doesn’t tell me the ward I come under

<!---->

> I want to know the name of the ward

<!---->

> It should say which ward I vote in.


or who their candidates are:

> I want to know who the is standing. I am going round in council circles

<!---->

> You don't tell us anything about the candidates.

<!---->

> Be useful to know who the candidates are, especially for the elderly.


Some also wanted more basic information:

> Link to candidates? Information about what the election is for?


We do link users to [WhoCanIVoteFor.co.uk](https://whocanivotefor.co.uk/) for information on their candidates, but it is fairly low down the page. The pattern we are seeing here is slightly different for local elections than the pattern we saw around last year's general election. In 2017, only a tiny proportion of comments requested this information, but more users requested this information in 2018 for local elections. This may indicate that there is more information available about national elections, or that voters are more likely to vote along party lines in national elections. Either way, there is some evidence that our approach to showing additional information about the election might need to be different for local and general elections in order to deliver value to users.

## Why do people use Where Do I Vote?

We received limited feedback about this, but broadly we observed the same themes this year as we did around the 2017 general election. The site was useful for people who lost their polling card or weren't sent one:

> I almost didn't vote because I didn't know where to go and have lost my polling card. thanks!

<!---->

> I haven’t received my polling card and was worried I couldn’t vote


or who had recently moved:

> I moved since the last elections, thanks for making this data so easily available!

<!---->

> I recently moved

Unlike in 2017, we didn't receive any explicit comments from first-time voters. This perhaps indicates lower levels of interest in local elections amongst younger voters, or is possibly just a symptom of the more limited pool of feedback we have to draw from.


## What next?

After collecting feedback in 2017, we came away from the process with a laundry list of improvements to make as a result. There is definitely some work we can do around presenting a bit more information around local elections in future, but the broad pattern we've observed this year is that the improvements we have made over the last year have effectively addressed problems and increased satisfaction with the website. There is still plenty left for us to do though. As well as continuing to monitor website feedback and error reports, there are a number of other research topics we will be looking at in order to keep improving our service:

What can we do to improve our service for data re-users? We've spent a lot of time thinking about how to improve the user experience for users of our own website, but more people now consume our polling station data via third party sites which use our API. Are we meeting the needs of our data/API consumers and how can we work with a wider range of partners to bring this information to an even wider audience?

A substantial number of users now find their polling station using our javascript widget. This allows councils, local media outlets and other third parties to embed a finder in their own website, but we have relatively little feedback on this. How can we collect feedback on this or apply the things we've learned from collecting feedback on [wheredoivote.co.uk](https://wheredoivote.co.uk/) to this increasingly important part of our offering?

The most important thing we can do to provide value to users is to answer the question "Where Do I Vote?". This year, we were able to serve a higher proportion of users with an answer than ever before. How can we remove the remaining barriers that prevent some councils for wanting or being able to share data with us? As we need to process and check an increasingly large amount of data, how can we improve our processes behind the scenes to do this efficiently in a short space of time?
