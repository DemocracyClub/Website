from django.db import models

class Card(models.Model):
    trello_id = models.CharField(blank=True, max_length=100, primary_key=True)
    title = models.CharField(blank=True, max_length=800)
    text = models.TextField(blank=True)
    weight = models.FloatField()
    url = models.URLField(blank=True)
    labels = models.ManyToManyField('backlog.CardLabel')
    published = models.BooleanField(default=True)
    comment_count = models.IntegerField(blank=True, null=True)
    cta_url = models.URLField(blank=True, max_length=800)
    time_required = models.CharField(blank=True, max_length=100)

    class Meta:
        ordering = ('weight', )

    def __str__(self):
        return self.title

    def get_cta_url(self):
        if self.cta_url:
            return self.cta_url
        return self.url

class CardLabel(models.Model):
    trello_id = models.CharField(blank=True, max_length=100, primary_key=True)
    name = models.CharField(blank=True, max_length=100)
    colour = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


    # {
    #     "id": "58bd63361db95c69861b68da",
    #     "checkItemStates": null,
    #     "closed": false,
    #     "dateLastActivity": "2017-03-06T13:31:34.348Z",
    #     "desc": "I think I can add loads of text here! I think I can add loads of text here! I think I ",
    #     "descData": {
    #       "emoji": {}
    #     },
    #     "idBoard": "58bd617ff04f88665a94c21a",
    #     "idList": "58bd618abc9a825bd64b5d8f",
    #     "idMembersVoted": [],
    #     "idShort": 1,
    #     "idAttachmentCover": null,
    #     "manualCoverAttachment": false,
    #     "idLabels": [],
    #     "name": "Testing",
    #     "pos": 65535,
    #     "shortLink": "9MpOwQpv",
    #     "badges": {
    #       "votes": 0,
    #       "viewingMemberVoted": false,
    #       "subscribed": false,
    #       "fogbugz": "",
    #       "checkItems": 0,
    #       "checkItemsChecked": 0,
    #       "comments": 0,
    #       "attachments": 0,
    #       "description": true,
    #       "due": null,
    #       "dueComplete": false
    #     },
    #     "dueComplete": false,
    #     "due": null,
    #     "idChecklists": [],
    #     "idMembers": [],
    #     "labels": [],
    #     "shortUrl": "https://trello.com/c/9MpOwQpv",
    #     "subscribed": false,
    #     "url": "https://trello.com/c/9MpOwQpv/1-testing"
    #   }
