import json
from django.contrib.auth.models import User
from .models import Interview, Question, QuestionReply


def get_user(userid):
    if userid != 0:
        u = User.objects.filter(id=userid).first()
    else:
        u = User.objects.filter(username='anonymous').first()
    return u


def get_question(qid):
    q = Question.objects.filter(id=qid).first()
    return q


def add_reply(u, q, reply):
    
    try:
        QuestionReply.objects.filter(user=u, question=q).delete()
        jreply = {'reply': reply}
        qr = QuestionReply(user=u, question=q, reply=jreply)
        qr.save()
    except Exception:
        return dict(status=False, error_id=6, msg='Commit new intery is Failure')
    
    return dict(status=True,)


def reply_question(d):
    
    u = get_user(d['userid'])
    
    if u is None:
        return dict(status=False, error_id=1, msg='User not found in system')
    
    q = get_question(d['question'])
    
    if q is None:
        return dict(status=False, error_id=2, msg='Question not found in system')
    
    if q.type == 1 and not isinstance(d['reply'], str):
        return dict(status=False, error_id=3, msg='Reply must be string')
    #if q.type == 2 and not isinstance(reply, int):
    #    raise 'Reply must be integer'
    #    return dict(status=False, error_id=4, msg='Reply must be integer')
    if q.type == 3 and not isinstance(d['reply'], list):
        return dict(status=False, error_id=5, msg='Reply must be list')
    
    return add_reply(u, q, d['reply'])


def get_questionreply(u, q):
    qr = QuestionReply.objects.filter(user=u, question=q).first()
    return qr.reply



def parse_qr(uql):
    l = []
    for t in uql:
        interview = t[0].interview
        reply = get_questionreply(t[1], t[0])
        r = {'interview': {'id': interview.id, 'name': interview.name},
             'question': {'id': t[0].id,
                          'text': t[0].text,
                          'type': t[0].type},
             'reply': reply}
        if t[0].type != 1:
            r['question']['variants'] = [dict(uid=e.uid, text=e.text) for e in t[0].variant.all()]
        l.append(r)
    return l
    
