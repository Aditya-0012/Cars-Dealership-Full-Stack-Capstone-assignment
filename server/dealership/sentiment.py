POSITIVE={'amazing','best','excellent','fantastic','friendly','good','great','helpful','love','perfect','professional','recommend','smooth','wonderful','fast','courteous','satisfied','awesome'}
NEGATIVE={'awful','bad','broken','disappointing','hate','horrible','late','poor','rude','slow','terrible','unhelpful','worst','waste','expensive'}
def analyze_sentiment(text):
    tokens=[w.strip(".,!?;:'\\\"()[]{}-").lower() for w in text.split()]
    pos=sum(w in POSITIVE for w in tokens); neg=sum(w in NEGATIVE for w in tokens)
    sentiment='positive' if pos>neg else 'negative' if neg>pos else 'neutral'
    return {'sentiment':sentiment,'score':round((pos-neg)/max(pos+neg,1),2),'positive_words':pos,'negative_words':neg}
