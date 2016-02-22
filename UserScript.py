
# coding: utf-8

# In[8]:


users="email@email.com:Stu Dent:Stu:Dr.Who:teamdrwho:xxxxx"

userdict={}
userdict['email'] = users.split(':')[0]
userdict['name'] = users.split(':')[1]
userdict['username'] = users.split(':')[2]
userdict['pname'] = users.split(':')[3]
userdict['group'] = users.split(':')[4]
userdict['passcode'] = users.split(':')[5]



quotes="""
I woke up and realized life is great and people are awesome and life is worth living.:
To all my little Hulkamaniacs, say your prayers, take your vitamins and you will never go wrong.:
You can have a wrestling idea, but you need to have these momentum-shifting moves. We had the Hulkamania movement, then it shifted to the beer-drinking, Stone Cold era, we reinvented the business with growing the black beard and becoming the bad guy, what's that next level.:The only time I'm not Hulk Hogan is when I'm behind closed doors because as soon as I walk out the front door, and somebody says hello to me, I can't just say 'hello' like Terry. When they see me, they see the blond hair, the mustache, and the bald head, they instantly think Hulk Hogan.:I fear no man, no beast or evil, brother.:If anybody dared say wrestling was fake, you'd punch 'em. And you never used the word show. If you used the word show it was an insult.:Ultimate Warrior had a hell of a gimmick, but wrestling is about so much more than that. You have to be consistent, work main events every night and have matches that people really believe in and want to see.:I train all the time and the weird thing is I'm in the gym with people between 20 and 25 years old and I look in the mirror and I look better than they do and they are young kids - either they haven't trained hard enough or they aren't serious enough.:I feel really good right now. It will really be a tough decision. It's so hard to give up what you love doing. Hanging up the boots will not be an easy thing to do.:Shawn Michaels is a born-again Christian, but inside he's the same old Shawn Michaels. He hasn't changed a bit.:They googled Hulk Hogan and there were 4,000 different websites and one guy was making like two and a half million dollars, three million dollars a year just selling my merchandise. We had to shut him down but he was making some serious money just selling my stuff.:Negativity and Hulkamania - 2 things that don't go together.:I promised each and every Hulkamaniac when I went to that great battlefield in the sky I would bring the WWF title with me.:I'm happy now.:Then as I was wrestling as Terry Boulder. I was on a talk show with Lou Ferrigno, and I was actually bigger than he was! I went back to the dressing room that night and all of the wrestlers go 'Oh my God you're bigger than the hulk on TV' so they started calling me Terry 'The Hulk' Boulder.:
Hopefully I can become the Babe Ruth of the World Wrestling Federation and be the champion at the same time.:I've been around so long and no matter if I've done good things or bad things, or my personal life has been good or bad, the fans have always stuck with me.:I love to give the fans what they want. They're what I miss most when I'm not wrestling. That time in the ring is like being in heaven for me.
"""



def create_mailscript(users):
    "users:emailofuser,nameofuser,user,piuser,group,passcode"
    import random 
    email, name, user, pimail, group, passwd = users.split(':')
    mailscript="""
    Dear %s
    
    User credentials for the Hulkster: 
    -----------------------------------
    user email: %s
    user name: %s
    group %s
    passcode: %s (will have to change upon first login)
    ssh %s@129.219.45.246
    
    Ground Rules: 
    -------------
    1. Do not give you password to anyone. 
    2. Do not run heavy computations on the login node. 
       - You can see the list of available compute nodes using the command diagnose -n and ssh into a node
       (e.g. ssh compute 0-0)
    3. There is currently NO backup scheme, coming soon. So make frequent backups of your data. 
    
    Sample Job Script 
    -----------------
    #!/bin/bash
    #$ -cwd
    #$ -V
    #$ -N TEM1_ENCA1
    #$ -S /bin/bash
    #$ -pe hmpich 42
    #$ -o myprog.out
    #$ -e mpprog.err

    module load opt-python 
    module load /share/apps/modules/modulefiles/mpich2
    module load /share/apps/modules/modulefiles/amber14
    python -V 
    mpiexec -np $NSLOTS zammain.py
    
    You can contacts me at akumar67@asu.edu for any questions/comments/suggestions. 
    
    --Avishek Kumar 
    
    %s --Hulk Hogan 
     
    """%(name, email, user, group, passwd, user,random.choice(quotes.split(':')))
    print mailscript 
    with open('tempscrpt.txt', 'w') as outfile:
              outfile.write(mailscript)
    
    
    
def send_email(userdict):
    bashcmd='cat tempscrpt.txt | mail -s \"Hulkster account: %s\" %s'%(userdict['name'],userdict['email'])
    print bashcmd 
    import os 
    os.system(bashcmd)



