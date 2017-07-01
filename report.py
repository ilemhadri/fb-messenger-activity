import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as plots2pdf
import numpy as np
import pandas as pd
import sys

#retrieve user id given user's name
#for this to work you need to enter the user's name in the form "firstname lastname" exactly as it appears on Facebook
def finduserid(name,profiles):
    try:
        return next(key for key in profiles if profiles[key]['name']==name.strip(' '))
    except:
        print "no user found"
        raise KeyError
        
# report of user activity
def reportid(userid,profiles,times):
    assert(type(userid) is str)
    if not userid in profiles:
        print('user not found in database. Have you checked that the user\'s id or name is correct?')
        sys.exit()
    # load data into pandas Series
    t=pd.Series( map(lambda x:pd.to_datetime(x,unit='s'),times[userid][1:]) )
    # group the data by day
    t1=t.groupby(t.apply(lambda s:s.replace(second=0,minute=0,hour=0)))
    p1=profiles[userid]

    dayindex=sorted(t1.groups.iteritems(),key=lambda x:x[0])
    #plot active times per day and save them to a pdf file
    pdf=plots2pdf.PdfPages('out/'+p1['name']+'.pdf')
    fig,ax = plt.subplots(figsize=(16,1.5))
    text="Messenger report by Ismael Lemhadri. " \
    "Copyright 2017 - https://ilemhadri.wordpress.com. All rights reserved. \n" \
    "Activity report for user %s from %s to %s. \n User profile: %s .\n User ID: %s .\n Uses the mobile Messenger app: %s ."%(p1['name'],str(dayindex[0][0])[:10],str(dayindex[-1][0])[:10],p1['uri'],userid,['NO','YES'][p1['is_messenger_user']]) 
    ax.text(0.06,0.06,text,color='purple')
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    pdf.savefig()
    for day,index in dayindex:
        fig,ax = plt.subplots(figsize=(16,1.2))
        t2=map(lambda s:pd.to_datetime(s),t[index].values)
        ax.set_xlim((t2[0].replace(hour=0,minute=0,second=0),t2[0].replace(hour=23,minute=59,second=59)))
        #compute time spent online
        to=str(np.sum([t2[i+1]-t2[i] for i in range(len(t2)-1) if (t2[i+1]-t2[i]<=pd.tslib.Timedelta(minutes=12))]))[7:]
        ax.set_title(str(day)[:10]+'\n Estimated time online: %s'%( to if len(to) else "a few minutes"))
        ax.yaxis.set_visible(False)
        ax.scatter(t2,[0]*len(t2),color='purple')
        plt.tight_layout()
        pdf.savefig()
    pdf.close()
    print ("Successfully generated %s\'s report!"%p1['name'])
    return
    
def report(name,profiles,times):
    return reportid(finduserid(name,profiles),profiles,times)