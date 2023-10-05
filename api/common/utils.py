from news.models import Medium, Party, PartyMediumScore
def fake_party_medium_scores():
    score=-1
    for party in Party.objects.all():
        for medium in Medium.objects.all():
            PartyMediumScore.objects.create(
                party=party,
                medium=medium,
                score=score,
                neutral_score=score
            )
            if score < 0:
                score = 1
            else:
                score = -1
