o
    ?x?b??  ?                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dl
mZ d dlmZ d dlmZmZmZ d dl	mZmZmZmZ d dlmZ d dlmZmZmZmZmZmZmZ d dlZd dlmZ d d	l m!Z! d d
l m"Z" d dl#m$Z$m%Z%m&Z&m'Z'm(Z(m)Z)m*Z*m+Z+m,Z,m-Z-m.Z.m/Z/ d dl0m1Z1m2Z2 d dl3m4Z4 d dl m"Z"m5Z5 d dlm6Z6m7Z7m8Z8 d dl9m:Z: d dl;m<Z<m=Z=m>Z>m?Z?m@Z@mAZAmBZBmCZC d dlDmEZE dZFdZGdZHdZIdZdZJdZKdZLejM?Nd?s?e?Od? ejM?Nd??sePdd? dd? ZQd d!? ZRd"d#? ZSd$d%? ZTd&d'? ZUd(d)? ZVd*d+? ZWd,d-? ZXd.d/? ZYd0d1? ZZd2d3? Z[d4d5? Z\e?  ej]Z^ej_Z`ejaZbejcZdejeZKejfZge`ebedeKeggZhd6d7? Zid8d9? Zjd:d;? Zkd<d=? Zld>d?? Zmd@dA? ZndBdC? ZodDdE? ZpdFdG? ZqdHdI? ZrdJdK? Zses?  dS )L?    N)?reader)?sleep)?MINYEAR?datetime?	timedelta)?Fore?Back?Style?init)?TelegramClient)?	functions?typesr   ?
connection?sync?utils?errors)?LeaveChannelRequest)?ReportSpamRequest)?GetDialogsRequest)?InputPeerEmpty?UserStatusOffline?UserStatusRecently?UserStatusLastMonth?UserStatusLastWeek?PeerUser?PeerChannel?InputPeerChannel?InputPeerUser?ChannelParticipantsAdmins?UserStatusOnline?UserStatusEmpty)?GetContactsRequest?DeleteContactsRequest)?DeletePhotosRequest)r   ?ImportChatInviteRequest)?GetFullChannelRequest?JoinChannelRequest?InviteToChannelRequest)?SessionPasswordNeededError)?UsernameInvalidError?ChannelInvalidError?PhoneNumberBannedError?YouBlockedUserError?PeerFloodError?UserPrivacyRestrictedError?ChatWriteForbiddenError?UserAlreadyParticipantError)?StringSessionz	@notoscami??? Z d038e172eb99839b69c39c3c25cd98cfi(? z[1;31mz[1;32mz[1;36mz[1,35mz
./sessions?	phone.csv?wc                  C   s?   t ?  tdd??R} dd? t?| ?D ?}d}|D ]9}t?|?}|d7 }ttjt	j
 d|? ? ? td|? ?tt?}|?|? |td	?? |td
?? |??  t?  qd}W d   ? n1 s]w   Y  t|rmtjt	j d nd? ttjt	j d ? t?  d S )Nr2   ?rc                 S   ?   g | ]}|d  ?qS ?r   ? ??.0?rowr7   r7   ?&/storage/emulated/0/fls/hackingzone.py?
<listcomp>+   ?    zlogin.<locals>.<listcomp>r   ?   ?Login ?	sessions/?@The_Hacking_Zonez@TeleModsApkTzAll Number Login Done !?Error!zPress Enter to back)?banner?open?csvr   r   ?parse_phone?printr	   ?BRIGHTr   ?GREENr   ?API_ID?HashID?startr&   ?
disconnect?RESET?YELLOW?input)?f?str_list?po?pphone?phone?client?doner7   r7   r;   ?login%   s&   

?
rX   c               
   C   s?  t t?} tt?}g }d}tdd???}dd? t?|?D ?}d}|D ]T}|d7 }t?|?}t	d|? ?? t
d	|? ?| |?}	|	??  |	?? sqzt	d
? t|?}
t|?}|?|? W q  typ   t	d? t|?}
t|?}|?|? Y q w t	?  q d}t	d? t	|ddi? t	d? tdddd??}tj|ddd?}|?|? W d   ? n1 s?w   Y  W d   ? n1 s?w   Y  dd? }dd? }|?  |?  t|r?d? d S d? d S )NFr2   r4   c                 S   r5   r6   r7   r8   r7   r7   r;   r<   D   r=   zBanFilter.<locals>.<listcomp>r   r>   r?   r@   zThis Phone Has Been RevokedZBanTzList Of Banned Numbers?sep?
zSaved In BanNumers.csv?BanNumbers.csvr3   ?UTF-8??encoding?,?Z	delimiter?lineterminatorc               	   S   s^  g } g }g }g }g }t dd??}|D ]}| ?|? qW d   ? n1 s$w   Y  | D ]}t|??dd?}|?|? q+t d??+}t dd??}	|D ]}|	?|?dd?? qHW d   ? n1 s^w   Y  W d   ? n1 smw   Y  t dd??}	|	D ]}
|?|
? qzW d   ? n1 s?w   Y  |D ]}t|??dd?}|?|? q?t|?}t|?}|?|?}|D ]}||vr?|?|? q?t d	dd
d??}tj|dd?}|?	|? W d   ? n1 s?w   Y  t d	??0}t dd??}|D ]}t|??dd?}|?|? q?W d   ? n	1 ?s	w   Y  W d   ? n	1 ?sw   Y  t
?d? t
?d	d? td? d S )Nr2   r4   rZ   ? r[   zoutfile.csvr3   r_   ?	unban.csvr\   r]   )ra   z(Done,All Banned Number Have Been Removed)rD   ?append?str?replace?write?set?intersectionrE   ?writer?	writerows?os?remove?renamerG   )Z
collectionZncZcollection1Znc1Zmaind?infile?line?xZmod_x?outfileZline1?iZmod_i?uniqueZunique1Zitd?	writeFilerj   Zlast?finalZline3r7   r7   r;   ?
autoremovel   sd   ????? ??

????? 
zBanFilter.<locals>.autoremovec               	   S   s?   dd l } dd l}td??+}tdd??}|D ]}|?|?dd?? qW d   ? n1 s+w   Y  W d   ? n1 s:w   Y  |?d? |?dd? td? d S )Nr   r2   rc   r3   r_   rb   Zcomplete)rE   rl   rD   rg   rf   rm   rn   rG   )rE   rl   ro   rr   rp   r7   r7   r;   ?dellst?   s   ??? 
zBanFilter.<locals>.dellst?Done!rB   )?intrJ   re   rK   rD   rE   r   r   rF   rG   r   ?connect?is_user_authorizedrd   r+   rj   rk   rP   )?api_id?api_hashZMadeByHackingZonerW   rQ   rR   rS   Zunparsed_phonerU   rV   ?HackingZoneZNero_opru   rj   rw   rx   r7   r7   r;   ?	BanFilter<   sV   


?	???)4r?   c               
   C   sV  t ?  d} d}d}d}d}tdd??}}dd	? t?|?D ?}d}|D ]f}t?|?}	|d
7 }ttjt	j
 dtj? dtjt	j ? d|	? ? ? td|	? ?tt?}
|
?|	? |
tjjdd?? |
?| d? t?d
? t|
?| ??}||v rzt|? |d
7 }ntd? |
??  t?  d}q!W d   ? n1 s?w   Y  t|? d?? t|r?d? d S d? d S )NZSpamBotuT   Good news, no limits are currently applied to your account. You’re free as a bird!Zbirdr   Fr2   r4   c                 S   r5   r6   r7   r8   r7   r7   r;   r<   ?   r=   z"SpamBotChecker.<locals>.<listcomp>r>   r?   ? r@   z@SpamBot??idz/startzyou are limitedTz - Accounts Are Usablery   rB   )rC   rD   rE   r   r   rF   rG   r	   rH   r   rI   ?	RESET_ALLrN   r   rJ   rK   rL   r   ?contactsZUnblockRequest?send_message?timer   re   ?get_messagesrM   rP   )?bot?mr   r4   rW   rQ   rR   rS   rT   rU   rV   ?msgr7   r7   r;   ?SpamBotChecker?   s<   
0


??r?   c                     s?  t ?? } | ?d? | d d ?? }|?d?}| d d ?? }ttjtj	 d|? ? ? t
d|? ?tt?}|??  |?? rB|?|? ?}d? g }|j|d	d
?}|t|??}|jj}? ?fdd?}	tdddd??N}
tj|
ddd????g d?? z.t|?D ]'\}}t|d ? d|? ?dd? |d dkr?td? |js?|	||? ? d ? qzW n   td? Y W d   ? n1 s?w   Y  |
??  td? d S )N?
config.inir   ?	FromGroupr_   ?PhoneNumber?
Logging For r@   r>   T?Z
aggressivec              
      ?r   |j r|j }nd}t|jt?r#??? ||j|j|j| j|jj	g? d S ??? ||j|j|j| jt
|j?jg? d S ?Nrb   ??username?
isinstance?statusr   ?writerowr?   ?access_hash?
first_name?title?
was_online?type?__name__??group?memberr?   ??countrj   r7   r;   rg   ?   ?   (,zScraper.<locals>.write?data.csvr3   r\   r]   rZ   r`   ??sr. no.r?   ?user idr?   ?namer?   r?   ?/???end?d   r   ?   ?c
There was a FloodWaitError, but check data.csv. More than 95%% of members should be already added.?
Users saved in the csv file.
)?configparser?ConfigParser?read?strip?splitrG   r	   rH   r   rN   r   rJ   rK   r{   r|   ?
get_entity?iter_participantsr%   ?	full_chat?participants_countrD   rE   rj   r?   ?	enumerater   r?   ?close)?config?link1?linksrU   ?cr?   ?members?channel_full_info?contrg   rQ   ?indexr?   r7   r?   r;   ?Scraper?   sF   



??
??r?   c                     s.  t j ?? } | t jdd? }t?? }|?d? |d d ?? }|?d?}|d d ?? }tt	j
tj d|? ? ? td	|? ?tt?}|??  |?? rO|?|? ?}d? g }|j|d
d?}|t|??}	|	jj}
? ?fdd?}tdddd???}tj|ddd????g d?? zrt|?D ]k\}}t|d ? d|
? ?dd? |d dkr?td? |js?t|jt t!f?r?|||? ? d ? q?t|jt"?r?|jj#}|j$| j$ko?|j%| j%ko?|j&| j&k}|j$|j$ko?|j%|j%ko?|j&|j&k}|s?|r?|||? ? d ? q?W n   td? Y W d   ? n	1 ?sw   Y  |?'?  td? d S )Nr>   ?Zdaysr?   r   r?   r_   r?   r?   r@   Tr?   c              
      r?   r?   r?   r?   r?   r7   r;   rg     r?   zDailyFilter.<locals>.writer?   r3   r\   r]   rZ   r`   r?   r?   r?   r?   r?   r   r?   r?   r?   )(r   ?nowr   r?   r?   r?   r?   r?   rG   r	   rH   r   rN   r   rJ   rK   r{   r|   r?   r?   r%   r?   r?   rD   rE   rj   r?   r?   r   r?   r?   r?   r   r   r   r?   ?day?month?yearr?   )?today?	yesterdayr?   r?   r?   rU   r?   r?   r?   r?   r?   rg   rQ   r?   r?   ?dZ
today_userZyesterday_userr7   r?   r;   ?DailyFilter  sZ   





$$
??
??r?   c                     s(  t j ?? } | t jdd? }t?? }|?d? |d d ?? }|?d?}|d d ?? }tt	j
tj d|? ? ? td	|? ?tt?}|??  |?? rO|?|? ?}d? g }|j|d
d?}|t|??}	|	jj}
? ?fdd?}tdddd???}tj|ddd????g d?? zot|?D ]h\}}t|d ? d|
? ?dd? |d dkr?td? |js?t|jt t!t"f?r?|||? ? d ? q?t|jt#?r?|jj$}t%dd?D ]'}| t j|d? }|j&|j&ko?|j'|j'ko?|j(|j(k}|r?|||? ? d ? q?q?W n   td? Y W d   ? n	1 ?sw   Y  |?)?  td? d S )Nr>   r?   r?   r   r?   r_   r?   r?   r@   Tr?   c              
      r?   r?   r?   r?   r?   r7   r;   rg   ]  r?   zWeeklyFilter.<locals>.writer?   r3   r\   r]   rZ   r`   r?   r?   r?   r?   r?   r   r?   ?   r?   r?   )*r   r?   r   r?   r?   r?   r?   r?   rG   r	   rH   r   rN   r   rJ   rK   r{   r|   r?   r?   r%   r?   r?   rD   rE   rj   r?   r?   r   r?   r?   r?   r   r   r   r   r?   ?ranger?   r?   r?   r?   ?r?   r?   r?   r?   r?   rU   r?   r?   r?   r?   r?   rg   rQ   r?   r?   r?   rs   ?current_day?correct_userr7   r?   r;   ?WeeklyFilterC  s\   





$
??
??r?   c                     sH  t ?? } | ?d? | d d ?? }|?d?}| d d ?? }ttjtj	 d|? ? ? t
d|? ?tt?}|??  |?? rB|?|? ?}d? g }|j|d	d
?}|t|??}|jj}? ?fdd?}	tdddd??-}
tj|
ddd????g d?? |j|td?D ]}|js?|	||? ? d ? q|W d   ? n1 s?w   Y  |
??  td? d S )Nr?   r   r?   r_   r?   r?   r@   r>   Tr?   c              
      r?   r?   r?   r?   r?   r7   r;   rg   ?  r?   zScrapAdmin.<locals>.writer?   r3   r\   r]   rZ   r`   )r?   r?   r?   r?   z
name,groupr?   )?filterz
Admins saved in the csv file.
)r?   r?   r?   r?   r?   rG   r	   rH   r   rN   r   rJ   rK   r{   r|   r?   r?   r%   r?   r?   rD   rE   rj   r?   r   r?   r?   )r?   r?   r?   rU   r?   r?   r?   r?   r?   rg   rQ   r?   r7   r?   r;   ?
ScrapAdmin?  s8   



???r?   c                     s*  t j ?? } | t jdd? }t?? }|?d? |d d ?? }|?d?}|d d ?? }tt	j
tj d|? ? ? td	|? ?tt?}|??  |?? rO|?|? ?}d? g }|j|d
d?}|t|??}	|	jj}
? ?fdd?}tdddd???}tj|ddd????g d?? zpt|?D ]i\}}t|d ? d|
? ?dd? |d dkr?td? |js?t|jt t!t"t#f?r?|||? ? d ? q?t|jt$?r?|jj%}t&dd?D ]'}| t j|d? }|j'|j'ko?|j(|j(ko?|j)|j)k}|r?|||? ? d ? q?q?W n   td? Y W d   ? n	1 ?sw   Y  |?*?  td? d S )Nr>   r?   r?   r   r?   r_   r?   r?   r@   Tr?   c              
      r?   r?   r?   r?   r?   r7   r;   rg   ?  r?   zMonthlyFilter.<locals>.writer?   r3   r\   r]   rZ   r`   r?   r?   r?   r?   r?   r   r?   ?   r?   r?   )+r   r?   r   r?   r?   r?   r?   r?   rG   r	   rH   r   rN   r   rJ   rK   r{   r|   r?   r?   r%   r?   r?   rD   rE   rj   r?   r?   r   r?   r?   r?   r   r   r   r   r   r?   r?   r?   r?   r?   r?   r?   r7   r?   r;   ?MonthlyFilter?  s\   





$
??
??r?   c                     sd  t j ?? } | t jdd? }t?? }|?d? |d d ?? }|?d?}|d d ?? }tt	j
tj d|? ? ? td	|? ?tt?}|??  |?? rO|?|? ?}d? g }|j|d
d?}|t|??}	|	jj}
? ?fdd?}tdddd???}tj|ddd????g d?? z?g }g }t|?D ]o\}}t|d ? d|
? ?dd? |?|? |d dkr?td? |js?t|j t!t"t#t$f?r?|||? ? d ? |?|? q?t|j t%?r?|j j&}t'dd?D ]#}| t j|d? }|j(|j(ko?|j)|j)ko?|j*|j*k}|r?|?|? q?q?|D ]}||v?r|||? ? d ? q?W n   td? Y W d   ? n	1 ?s#w   Y  |?+?  td? d S )Nr>   r?   r?   r   r?   r_   r?   r?   r@   Tr?   c              
      r?   r?   r?   r?   r?   r7   r;   rg   
  r?   zNonActive.<locals>.writer?   r3   r\   r]   rZ   r`   r?   r?   r?   r?   r?   r   r?   r?   r?   r?   ),r   r?   r   r?   r?   r?   r?   r?   rG   r	   rH   r   rN   r   rJ   rK   r{   r|   r?   r?   r%   r?   r?   rD   rE   rj   r?   r?   rd   r   r?   r?   r?   r   r   r   r   r   r?   r?   r?   r?   r?   r?   )r?   r?   r?   r?   r?   rU   r?   r?   r?   r?   r?   rg   rQ   Z	all_usersZactive_usersr?   r?   r?   rs   r?   r?   r7   r?   r;   ?	NonActive?  sl   





$
?

??
??r?   c                  C   s?  t jt jd? t?? } | ?d? | d d ?? }| d d ?? }tdddd	??}t?	|?}d
d? |D ?}W d   ? n1 s>w   Y  tdddd	??}t?	|?}dd? |D ?}W d   ? n1 saw   Y  t
d|? ?tt?}|??  |?? s?td|? d?? n?g }d }	d}
g }d}|dk?rVz?|?|?}|jdk?rt|j?}|j|dd?}g }g }d}g }|D ]}zt|j?|v r?|?|?t|j??? W q?   td? Y q?|??  |??  |jdd? |D ]}||= q?tddddd??}t?|?}|?|? W d   ? n	1 ?sw   Y  d}n
ttjtj d ? d}W n7 t j!j"j#?y-   |t$|?? Y n% t%?yB   ttjtj& d ? d}Y n   ttjtj d ? d}Y |dks?t'? }dd? }d d!? }|?  |?  td"dd#d	??X}t?	|?}tddd#d	??;}tj|d$d%d&?}|?(g d'?? d}|D ]}|d(7 }|?(||d( |d) |d* |d+ |d, |d- f? ?q?W d   ? n	1 ?s?w   Y  W d   ? n	1 ?s?w   Y  t)?*d.? t)?*d"? ttjtj+ d/ ? ttjtj& d0 ? ttjtj, d1 ? t-?  d S )2N)?levelr?   r   ?ToGroupr?   r?   r4   zutf-8r]   c                 S   ?   g | ]}|?qS r7   r7   ?r9   rs   r7   r7   r;   r<   F  ?    z(DeleteALreadyMembers.<locals>.<listcomp>c                 S   s   g | ]}t |d  ??qS )?   )re   r?   r7   r7   r;   r<   J  s    r@   z
Login fail, for number z need Login first
??   r   ?????Ti?  ??limitzError get user)?reverser3   rb   )r^   ?newlinez
Invalid Group..
z
Only Public Group Allowed..
z
Invalid Group....
c                  S   ??   t ? } tdddd??%}t?|?}|D ]}| ?|? |D ]}|dkr&| ?|? qqW d   ? n1 s2w   Y  tdddd??}tj|dd	d
?}|?| ? W d   ? d S 1 sWw   Y  d S ?Nr?   r4   r\   r]   rb   ?1.csvr3   r_   rZ   r`   ??listrD   rE   r   rd   rm   rj   rk   ??linesZreadFiler   r:   Zfieldru   rj   r7   r7   r;   ?main~  ?    


????"?z"DeleteALreadyMembers.<locals>.mainc                  S   r?   ?Nr?   r4   r\   r]   r?   ?2.csvr3   r_   rZ   r`   r?   r?   r7   r7   r;   ?main1?  ?    


????"?z#DeleteALreadyMembers.<locals>.main1r?   r\   r_   rZ   r`   )r?   r?   r?   r?   r?   r?   ZStatusr>   r?   r?   ?   ?   ?   r?   zAlready Member Deleted Done !zTask CompletedzPress Enter to exit).?loggingZbasicConfigZWARNINGr?   r?   r?   r?   rD   rE   r   r   rJ   rK   r{   r|   rG   r?   ?	megagroupre   r?   ?get_participantsrd   r?   r?   rM   ?sortrj   rk   r	   rH   r   ?RED?telethonr   Zrpcerrorlistr/   r&   ?
ValueErrorrI   r?   r?   rl   rm   rN   rO   rP   )r?   ?linkrU   rQ   Zusers1?usersZuserlistrV   ?chats?	last_date?
chunk_size?groups?nr?   Zgroup_id?all_participants?resultsZresults1r?   Zindex1?userrs   rg   r?   r?   r?   ?source?rdrrj   r:   r7   r7   r;   ?DeleteALreadyMembers6  s?   

?
?


?
??%
4????


r	  c                  C   s?   d} t dd??O}dd? t?|?D ?}d}|D ]8}t?|?}|d7 }ttjtj	 d|? ? ? t
d	|? ?tt?}|?|? |tjj|?d
?d??}td? d} qW d   ? n1 sYw   Y  t| rfd? d S d? d S )NFr2   r4   c                 S   r5   r6   r7   r8   r7   r7   r;   r<   ?  r=   zSetProfile.<locals>.<listcomp>r   r>   zChanging in r@   zuntamed.jpg)?filez"done! profile pic has been changedTry   rB   )rD   rE   r   r   rF   rG   r	   rH   r   rI   r   rJ   rK   rL   r   ZphotosZUploadProfilePhotoRequestZupload_filerP   )rW   rQ   rR   rS   rT   rU   rV   ?resultr7   r7   r;   ?
SetProfile?  s$   

???r  c                  C   s?   d} t dd??R}dd? t?|?D ?}d}|D ];}t?|?}|d7 }ttjtj	 d|? ? ? t
d	|? ?tt?}|?|? |t|?d
??? ttjtj d ? d} qW d   ? n1 s\w   Y  t| rid? d S d? d S )NFr2   r4   c                 S   r5   r6   r7   r8   r7   r7   r;   r<   ?  r=   z!DeleteProfile.<locals>.<listcomp>r   r>   zDeleting in r@   ?mezProfile Pic DeletedTry   rB   )rD   rE   r   r   rF   rG   r	   rH   r   r?   r   rJ   rK   rL   r#   Zget_profile_photosrI   rP   )rW   rQ   rR   rS   rT   rU   rV   r7   r7   r;   ?DeleteProfile?  s    

??r  c                  C   s@   dd l } g d?}|D ]}t| ?t?? |? t? ?? q
td? d S )Nr   )z  ___                  ___  z (o o)                (o o) z(  V  ) Hacking Zone (  V  ) z--m-m------------------m-m-- r?   )?randomrG   ?choice?colorsr  )r  ?b?charr7   r7   r;   rC   ?  s
   	rC   c               	      s?   t ?  tj?tj?tj?tj?tj?t?  g } g }g }tdd??}t	|?}t
|?}|D ]}|?t|d ?? q+W d   ? n1 sAw   Y  |?t?? d?? d?? tt|??? ?? ?? ? ??????fdd?????fdd	?? ??  d S )
Nr2   r4   r   ?Total account: r?   c                      s6  t t?? d?? ???d } t t?? d?? ???}t t?? d?? ???}t t?? d?? ???}tdddd	??}tj|d
dd?}|?||| g? W d   ? n1 sQw   Y  d}d}?| |? D ?]?}|d7 }td|? ?? t?|?}	tt	j
tj dt	j? dt	j
tj ? d|	? ? ? td|	? ?tt?}
|
??  |
?? s?t?? d?? ?? |
?|	? |
?|	td?? d}g }t|dd	??;}tj|d
dd?}t|d ? |D ]#}i }|d |d< |d |d< t |d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?s&w   Y  t |?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sZw   Y  t |?}|| }tdddd	??}tj|d
dd?}|?||g? W d   ? n	1 ?s?w   Y  d}|D ]y}t |?t |d ?k?r
t |d ?t |?k?r
z1|d7 }|d dk?r?t?? d?? ?? W ?q?|
tjj|d |d td?dd d!?? |? d"?}W n* tj?y? } z
|j j!}W Y d }~nd }~w   t"?#?  t?? d#?? ?? Y ?q?t|? ?q?|d7 }q`t$?%d? ? ?  d S )$N?From Account No : r>   ?Upto Account No : zFrom where you want to start : z3How many contacts you want to add in one Account : ?
memory.csvr3   r\   r]   r_   rZ   r`   r   ?Index : r?   r?   r@   ?some thing has changed?Enter the code: r?   ?srnor?   r?   r?   r?   r?   r4   rb   ?	Just Nextr   ZgdfT)r?   r?   ?	last_namerU   Zadd_phone_privacy_exception? - done?Unexpected Error)&rz   rP   rD   rE   rj   r?   rG   r   rF   r	   rH   r   rI   r?   rN   r   rJ   rK   r{   r|   ?send_code_request?sign_inr   ?nextrd   r?   r   r?   ZAddContactRequestre   r   ?RPCError?	__class__r?   ?	traceback?	print_excrl   rm   ) ?From?Upto?rex?hacksr
  rj   ?a?indexx?xdrU   rV   ?
input_filer?   rQ   ?rowsr:   r  ?hash_obj?
csv_reader?list_of_rows?
row_number?
col_number?numnext?	startfrom?	nextstart?numend?endto?nextend?df?itr?   ?e)?again?bl?grr  rT   r4   ?yer7   r;   ?autos  s?   ?
0

???	??,???


z"AutoaddContactPhone.<locals>.autosc                     s.   t ?? d?? ??} | dkr? ?  d S t?  d S )NzRDone!
Choose From Below:

1 - Repeat The Script
OR Just Hit Enter To Quit

Enter: ?1)rP   ?quit)?stat)rB  r  r4   r7   r;   r>  ?  s   

z"AutoaddContactPhone.<locals>.again)r
   r   ?LIGHTRED_EXrI   rN   ?BLUErO   rC   rD   r   ?tuplerd   rz   rG   re   ?len)r}   r~   rU   ?	delta_objr1  ?list_of_phone?phone_r7   )r>  rB  r?  r@  r  rT   r4   rA  r;   ?AutoaddContactPhone?  s,   ??(i
rM  c                  C   s?  t jdd? ttjtj d ? t? } t| ? d?d??}dd? t	?
|?D ?aW d   ? n1 s0w   Y  tdttt?? ? ttd	??d
 }ttd??}d}dat||? D ]y}|d
7 }td|? ?? t?|?}td|? ?? td|? ?tt?}|?|? |tdd??}d}	|jD ]E}
|	d
7 }	z|t|
gd?? ttjtj |	? d|
j? d? ? W q? tjy? } z|jj}t|	? d|
j? d|? ?? W Y d }~q?d }~ww qWd S )NT)Z	autoresetzEnter Accounts List : z.csvr4   c                 S   r5   r6   r7   r8   r7   r7   r;   r<   ?  r=   z!DeleteContact.<locals>.<listcomp>r  r  r>   r  r   r  r?   r@   ??hashr?   ? - z	 - DELETE)?coloramar
   rG   r	   rH   r   rI   rP   rD   rE   r   ?phlistre   rI  rz   ZHackingZonepror   rF   r   rJ   rK   rL   r!   r?   r"   r?   r   r#  r$  r?   )ZphonecsvrQ   Z HackingZone_ne_script_banaya_haiZ5telegram_script_banyane_ke_liye_HackingZone_ko_dm_kror,  ZHackingZoneonytrU   rV   r?   ZrexaddZrexopr=  ?error7   r7   r;   ?DeleteContact?  sB   ?


&????rT  c                   C   s?  t ?? } | ?d? | d d }| d d }| d d }| d d }| d d }tdd	??}d
d? t?|?D ?}W d   ? n1 sAw   Y  tdtt|?? ? tt	j
tj d ? t? }tt	j
tj d ? tt? ?}	tt	j
tj d ? tt? ?}
|dkr?t|?}|}n
|dkr?t|?}|}t|?}t|?d }t|?}d}da|||? D ?]}|d7 }t?|?}td|? ?? td|? ?tt?}|?|? td|? ?? z	|?t|??}W n3 t?y   |dkr?|t|?? |?t|??}n|dk?r
|t|?? t?d? |?t|??}Y nw |t|d??}t|jj ?atdt? ?? t|k?r4td|? d?? t?  t!?  |t"dd??}|j#}t|?}td|? ?? d}d}||k ?r?dd? |d |	? D ?}zDt?|
? |t$j%j&||d?? ||	7 }t'dd ?D ]}z||= W ?qv t(?y? } zW Y d }~?qvd }~ww tt	j
tj d!|? ? ? W n t)j*?y? } z|j+j,}tt|?? W Y d }~n
d }~ww ||k ?sRq?d S )"Nr?   r   r?   ?GroupID?	EnterStop?StartingAccount?
EndAccountr2   r4   c                 S   r5   r6   r7   r8   r7   r7   r;   r<   ?  r=   zBulkAdder.<locals>.<listcomp>r  z1Enter Y if group has private link else N (Y/N) : z.In A Batch How many Members You Want To Add : ?*Enter Delay Time Per Request 0 For None : ?Y?Nr>   r   r?   r@   r  r?   ??channel?	Members: ?The Goal Of ? Has Been CompletedrN  zTotal : c                 S   r?   r7   r7   )r9   Zdeltar7   r7   r;   r<   ?  r?   )r]  r?   ?
   zBATCH: )-r?   r?   r?   rD   rE   r   rG   re   rI  r	   rH   r   rI   rP   rz   ZLegenddev_is_main_developerr   rF   r   rJ   rK   rL   r?   r   r?   r$   ?get_input_entityr&   r?   r   r%   r?   r?   rD  r!   r?   r   ?channelsr'   r?   ?	Exceptionr   r#  r$  r?   ) r?   ?	grouplink?groupid?stopnum?stacno?endacnorQ   rR  ZprchkZLegenddevismain?HackingZone_devr?   Zprlink?stopZ
start_fromZuptor,  ZpythondeveloperrU   rV   r]  ?channelinfor?   Zuser_to_addZcountconZ
batchcountZlolZsemenrs   ?Dr=  rS  r7   r7   r;   ?	BulkAdder?  s?   
?





??	


?????
???rn  c            	         s?   t d? t tjtj d ? tt? ?} tdd??}t|?}t	|?}| }d}||d  |d  }W d   ? n1 s9w   Y  t
?t? |?t?? }|?d? |d d ?? ???fd	d
?}|?  d S )Nz"choose accout that are not limitedz'Which Account You Want To Use?

Enter: r2   r4   r>   r?   r   r?   c                     s?  t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw ?}td? g }|j
|dd?}td	? td
ddd??J}tj|ddd?}|?g d?? |D ]0}|jr{|j}nd}|jr?|j}	nd}	|jr?|j}
nd}
|	d |
 ?? }|?||j|j|g? qrW d   ? n1 s?w   Y  tdt? ?? |?? j}td|? dt? ?? d}d}ttdt? ???}g }td
dd??=}tj|ddd?}t|d ? |D ]%}i }|d |d< t|d ?|d< t|d ?|d< |d |d< |?|? q?W d   ? n	1 ?sw   Y  d}ttd t? ???}|D ]?}|dk?rH|d dk?r@?q0|?|d ?}n|dk?rWt|d |d ?}ntd!t? ?? |??  t ?!?  z!td"|d ? |?"||?#|d ?? td#?#|?? t$?%|? W ?q0 t&?y?   td$? td#?#|?? t$?%|? Y ?q0 t'?y? } ztd%|? td&? td#?#|?? t$?%|? W Y d }~?q0d }~ww |??  td'? td(? d S ))Nr@   zEnter code: rb   zEnter password: )?passwordzFetching Members...Fr?   zSaving In file...z	msend.csvr3   r\   r]   r_   rZ   r`   )r?   r?   zaccess hashr?   r?   zMembers scraped successfully.zMessage was sending throuh ?(   ?   z'Enter sleep time duration in messages :r   r?   r>   r?   r?   r?   r?   r?   zsend your messsagezInvalid Mode. Exiting.zSending Message to:zWaiting {} secondsz\Getting Flood Error from telegram. Script is stopping now. Please try again after some time.zError:zTrying to continue...z Done. Message sent to all users.z"
 Press enter to goto main menu...)(r   rF   r   r{   r|   r   r!  rP   rG   r(   r?   rD   rE   rj   r?   r?   r?   r  r?   r?   r?   ?lg?get_merA  rz   r   r"  rd   re   rb  r   rM   ?sys?exitr?   ?formatr?   r   r-   rd  )rU   rV   ro  ?target_groupr  rQ   rj   r  r?   r?   r  r?   ?acc_nameZSLEEP_TIME_2ZSLEEP_TIME_1Z
SLEEP_TIMEr?   r/  r:   ?mode?messageZreceiverr=  ?r~   r}   rT   Zto_groupr7   r;   ?	sedmrunal"  s?   

???

??



??z messagesender.<locals>.sedmrunal)rG   r	   rH   r   rO   rz   rP   rD   r   r?   rJ   rK   r?   r?   r?   )	ZLegend_devinputZread_objr1  r2  r3  r4  ?valuer?   r|  r7   r{  r;   ?messagesender  s$   
?

]r~  c                  C   st  t j} t j}t j}t j}t j}t j}t j}||||||g}t?	? }|?
d? |d d }	|d d }
|d d }|d d }|d d }g }tdd	???}t|?}t|?}|D ]}|?t|d
 ?? qV|}t|? d|? t|?? ?? tt|? d|? ???}tt|? d|? ???}d}t|? d|? t|?? |? d?? d
}d
}d
}|D ]?}|d7 }td|? ?? t?|?}td|? ?tt?}td|? |? |? d|? d?? |??  |?? ?r|?? j}z|td?? |?t|? td|? |? |? d?? |d7 }W n t ?y } zt|? ? W Y d }~q?d }~ww |d
k?rtd|? d?? q?td|? d?? q?W d   ? d S 1 ?s3w   Y  d S )Nr?   r   r?   rU  rV  rW  rX  r2   r4   r   ? Total accounts: z% Enter number of accounts to Report: z Send Message For Report r>   z -- Sending Reports from z account(s) --r  r@   ?User: ? -- ?Starting session... rA   zReport Done From: z  To Notoscam-- rZ   ?session endedzAll reports done sucesfully)!r   rN   rG  r?   ?WHITE?CYANrO   rI   r?   r?   r?   rD   r   rH  rd   rz   rG   rI  rP   re   r   rF   r   rJ   rK   rL   r|   rs  r?   r&   r?   ?scamrd  )r  rr  r4   r3   ?cyrA  r@  r  r?   re  rf  rg  rh  ri  rU   rJ  r1  rK  rL  rT   ?number_of_accsr  ?
sleep_time?send_status?approx_members_countr?   ?accr?   rx  r=  r7   r7   r;   ?ScamTag?  sl   
 



??
?$?r?  c                     sv  t ? } dd? }dd? }|?  |?  tdddd??V}t?|?}td	d
dd??:}tj|ddd?}|?g d?? d}|D ]}|d7 }|?||d |d |d |d |d |d f? q9W d   ? n1 sbw   Y  W d   ? n1 sqw   Y  t?d? t?d? t?  t	j
?t	j?t	j?t	j}	t	j?	t?? }
|
?d? |
d d ?|
d d ?|
d d ?|
d d ?|
d d ? g }tdd?? }t|?}t|?}|D ]}|?t|d ?? q?|?W d   ? n1 s?w   Y  t?? d?? d ?? tt|??? ?? ?? ? ?????????	f
d!d"?}? ?????????	f
d#d$?}tt|	? d%?? ???}|d&k?r/|?  d S |d'k?r9|?  d S d S )(Nc                  S   r?   r?   r?   r?   r7   r7   r;   r?   ?  r?   zAdder.<locals>.mainc                  S   r?   r?   r?   r?   r7   r7   r;   r?   ?  r?   zAdder.<locals>.main1r?   r4   r\   r]   r?   r3   r_   rZ   r`   r?   r   r>   r?   r?   r?   r?   r?   r?   r?   r   r?   rU  rV  rW  rX  r2   r  r?   c            )         s?  t tjtj d ? tt? ?} d}t??}t??}t??d }t? ?}td?}td?d }t??}tdddd??}	t	j
|	d	d
d?}
|
?||| g? W d   ? n1 sTw   Y  d}d}?||? D ?]?}|d7 }t d|? ?? t?|?}t d|? ?? td|? ?tt?}|??  |?? s?t ?? d?? ?? |?|? |?|td?? |}g }t|dd??;}t	j|d	d
d?}t|d ? |D ]#}i }|d |d< |d |d< t|d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sw   Y  t|?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sLw   Y  t|?}|| } tdddd??}!t	j
|!d	d
d?}
|
?|| g? W d   ? n	1 ?s{w   Y  |t|?? t?d? |?t|??}"|t|"d??}#t|#jj ?}$t d|$? ?? |$|k?r?t d|? d?? t?  t!?  d}%|D ]?}t|?t|d ?k?rZt|d ?t|?k?rZz2|%d7 }%|d dk?r?t ?? d?? ?? W ?q?|t"j#?$||d g?? t |%? d ?? t?| ? W ?q? t%?y& }& z|t|?? t?d? W Y d }&~&?q?d }&~&w t&j'?yG }' z|'j(j)}(t |%? d!|(? ?? W Y d }'~'?q?d }'~'w   t*?+?  t ?	? d"?? ?? Y ?q??q?|d7 }qct,?-d? d S )#NrY  r?   r>   ?2   r  r3   r\   r]   r_   rZ   r`   r   r  r?   r@   r  r  r  r?   r?   r?   r?   r?   r4   r?   r\  r^  r_  r`  rb   r  r  rP  r  ).rG   r	   rH   r   rI   rz   rP   re   rD   rE   rj   r?   r   rF   r   rJ   rK   r{   r|   r   r!  r   r"  rd   r?   r&   r?   r   rb  r   r%   r?   r?   rD  r   rc  r'   r/   r   r#  r$  r?   r%  r&  rl   rm   ))rj  r   ?rexlinkr?   r'  r(  r)  r*  rk  r
  rj   r+  r,  r-  rU   rV   r.  r?   rQ   r/  r:   r  r0  r1  r2  r3  r4  r5  r6  r7  r8  r9  r:  r;  r]  rl  ?rexprodeltanoobr<  ?cwfer=  r?   ?
ri  r@  rf  re  r  rT   r4   rh  rg  rA  r7   r;   rB    s?   
?


???	??

,
? ??
zAdder.<locals>.autosc            *         s?  t tjtj d ? tt? ?} d}t??}t??}t??d }t? ?}td?}td?d }t??}tdddd??}	t	j
|	d	d
d?}
|
?||| g? W d   ? n1 sTw   Y  d}d}?||? D ?]}|d7 }t d|? ?? t?|?}t d|? ?? td|? ?tt?}|??  |?? s?t ?? d?? ?? |?|? |?|td?? |}g }t|dd??C}t	j|d	d
d?}t|d ? |D ]+}i }|d |d< |d |d< t|d ?|d< t|d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?s w   Y  t|?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sTw   Y  t|?}|| } tdddd??}!t	j
|!d	d
d?}
|
?|| g? W d   ? n	1 ?s?w   Y  |tjj|d??}"t?d? |?t|??}#|t |#d??}$t|$j!j"?}%t d|%? ?? |%|k?r?t d|? d?? t?  t#?  d}&|D ]?}t|?t|d ?k?rlt|d ?t|?k?rlt d|%? ?? z2|&d7 }&|d d k?r?t ?? d!?? ?? W ?q?|tj$?%||d g?? t |&? d"?? t?| ? W ?q? t&?y8 }' z|t|?? t?d? W Y d }'~'?q?d }'~'w t'j(?yY }( z|(j)j*})t |&? d#|)? ?? W Y d }(~(?q?d }(~(w   t+?,?  t ?	? d$?? ?? Y ?qȐq?|d7 }qct-?.d? d S )%NrY  r?   r>   r?  r  r3   r\   r]   r_   rZ   r`   r   r  r?   r@   r  r  r  r?   r?   r?   r?   r?   r?   r4   rN  r?   r\  r^  r_  r`  rb   r  r  rP  r  )/rG   r	   rH   r   rI   rz   rP   re   rD   rE   rj   r?   r   rF   r   rJ   rK   r{   r|   r   r!  r   r"  rd   r?   r   ?messagesr$   r?   r   rb  r   r%   r?   r?   rD  rc  r'   r/   r   r#  r$  r?   r%  r&  rl   rm   )*rj  r   r?  r?   r'  r(  r)  r*  rk  r
  rj   r+  r,  r-  rU   rV   r.  r?   rQ   r/  r:   r  r0  r1  r2  r3  r4  r5  r6  r7  r8  r9  r:  r;  r  r]  rl  r?  r<  r?  r=  r?   r?  r7   r;   ?private?  s?   
?


???	???

,
? ??
zAdder.<locals>.privatez%Press Y if group is private else N : rZ  r[  )r?   rD   rE   r   rj   r?   rl   rm   r
   r   rF  rI   rN   rG  rO   r?   r?   r?   rH  rd   rz   rG   re   rI  rP   )r?   r?   r?   r  r  rQ   rj   rs   r:   r?  r?   rU   rJ  r1  rK  rL  rB  r?  Z	rexchooser7   r?  r;   ?Adder?  sd   
2????


?(yy



?r?  c                  C   s?   t ?  tdd??I} dd? t?| ?D ?}d}|D ]1}t?|?}|d7 }ttd|? ? ? td|? ?t	t
?}|?|? |?t?}tt|d j?  ? qW d   ? d S 1 sTw   Y  d S )	Nr2   r4   c                 S   r5   r6   r7   r8   r7   r7   r;   r<     r=   zViewotp.<locals>.<listcomp>r   r>   zGetting Telegram message Otp r@   )rC   rD   rE   r   r   rF   rG   r?  r   rJ   rK   rL   r?   ?chatoprA  ?text)rQ   rR   rS   rT   rU   rV   r?  r7   r7   r;   ?Viewotp  s   


?"?r?  c                  C   s?  t j} t j}t j}t j}t j}t j}t j}||||||g}t?	? }|?
d? |d d }	|d d }
|d d }|d d }|d d }g }tdd	???}t|?}t|?}|D ]}|?t|d
 ?? qV|}t|? d|? t|?? ?? tt|? d|? ???}tt|? d|? ???}d}t|? d|? |? d?? d
}d
}d
}|D ]l}|d }td|? ?? t?|?}td|? ?tt?}td|? |? |? d|? d?? |??  |?? ?r	|?? j}z|t|?? td|? d|? |? |? d?? |d7 }W q? t?y } zt|? ? W Y d }~q?d }~ww q?|d
k?r td|? d?? td|? d?? ntd|? d?? td|? d?? W d   ? d S W d   ? d S 1 ?sDw   Y  d S )Nr?   r   r?   rU  rV  rW  rX  r2   r4   r   r  z* Enter number of accounts to report spam  z% Enter Group,Channel or user usernamer>   z! --Report Spam Started Sucesfullyz account --?<   r  r@   r?  r?  r?  z=======Reported spam z:from z	======== rZ   r?  z Press enter to exit...z all reports done sucessfylly)r   rN   rG  r?   r?  r?  rO   rI   r?   r?   r?   rD   r   rH  rd   rz   rG   rI  rP   re   r   rF   r   rJ   rK   rL   r|   rs  r?   r   rd  )r  rr  r4   r3   r?  rA  r@  r  r?   re  rf  rg  rh  ri  rU   rJ  r1  rK  rL  rT   r?  r  r?  r?  r?  r?   r?  rk  r?   rx  r=  r7   r7   r;   ?
reportspam"  sr   




???

?#$?r?  c            #   
   C   sB  t j} t j}t j}tj}t?? }|?d? |d d ?	? }|?
d?}|d d ?	? }ttjt j d|? ? ? td|? ?tt?}|??  |?? r?td?}	|	d	krYttd
 t ? n|	dkrvttt? d| ? ???}
|tjj|
d??}t?d? g }d }d}g }|t|dt? |dd??}|?|j ? |?!? }td?}|d	kr?|D ]}z|j"dkr?|?#|? W q?   Y q?n|dkr?|D ]}z|j$j% W q?   |?#|? Y q?ttd t ? d}|D ]}ttd t t|? d d |j& ? |d7 }q?td? ttd t ?}|t'|? }ttd ? t?d? g }|j(|dd?}|?? ?r?d}t)j)?*? }|t+dd? }|t+d d? }t,d!d"d#d$?}t-j.|dd%d&?}|?/g d'?? |D ]N}|j0?rT|j0}nd}|j1?r^|j1}nd}|j2?rh|j2} nd} |d( |  ?	? }!t3|j%t4??r~|j%j5}"nt6|j%?j7}"|?/|||j8|j9|!|j&|"g? |d }?qJttd) ? d S )*Nr?   r   r?   r_   r?   r?   r@   z:1: Already Joined group Scrape 
2: Join group then Scrape
rC  z[+] openning scraper?2z Enter Group hashrN  r?   r?   r   )Zoffset_dateZ	offset_idZoffset_peerr?   rO  zE1: For only public Groups 
2: For all groups public and private both
Tz&[+] Choose a group to scrape members :?[?]rP  r>   rb   z[+] Enter a Number : z[+] Fetching Members...i|  r?   i????r?   i????r?   r3   r\   r]   rZ   r`   r?   r?   z![+] Members scraped successfully.):r   r?   rI   rG  r	   r?   r?   r?   r?   r?   r?   rG   rH   rN   r   rJ   rK   r{   r|   rP   r@  ?rere   r?  r   r?  r$   r?   r   r   r   ?extendr?   Zget_dialogsr?   rd   Zentityr?   r?   rz   r?   r   r?   r   rD   rE   rj   r?   r?   r?   r  r?   r   r?   r?   r?   r?   r?   )#r4   ?gr  r?   r?   r?   r?   rU   r?   ?pr?   r  r?   r   r  r  Zdialogsr?   Zchatrs   Zg_indexrw  r?   r?   r?   Z	last_weekZ
last_monthrQ   rj   r  r?   r?   r  r?   r?   r7   r7   r;   ?
pvtscraper]  s?   

?
?

??
&




r?  c                  C   s?  t ?  ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd	 t ? ttd
 t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd??} | dkr?t?  d S | dkr?t?  d S | d k?rt	?  d S | d!k?rt
?  d S | d"k?rt?  d S | d#k?r#t?  d S | d$k?r-t?  d S | d%k?r7t?  d S | d&k?rAt?  d S | d'k?rKt?  d S | d(k?rUt?  d S | d)k?r_t?  d S | d*k?rit?  d S | d+k?rst?  d S | d,k?r}t?  d S | d-k?r?t?  d S | d.k?r?t?  d S | d/k?r?t?  d S | d0k?r?t?  d S | d1k?r?t?  d S | d2k?r?t?  d S | d3k?r?t?  d S d S )4Nz[A] ~/Choose an Option\~z[1] ~Login~z[2] ~Ban Filter + Remover~z[3] ~Spambotchecker + Remover~z"[B] ~/Advanced Scraper & Filters\~z[4] ~Scraper~ z[5] ~Private Scraper~ z[6] ~Daily Filter~ z[7] ~Weekly Filter~ z[8] ~Scrap Admin~ z[9] ~Monthly Filter~ z[10] ~NonActive Filter~ z[11] ~Deletealreadynumbers~ z[C] ~/Profile Pic Change\~z[12] ~Set profile Pic~z[13] ~delete profile Pic~z[D] ~/Contact Adder Option\~z![14] ~Autoaddcontact - For Phone~z[15] ~Deletecontact~  z [E] ~/Additional Adder options\~z[16] ~Bulk Adder~z[17] ~Adder {Best}~z[F] ~/Additional Options\~z[18] ~Telegram OTP viewer~z[19] ~Send Message~z[20] ~Report Spam A User~z[21] ~ScamTag~z[22] ~Exit~z
Enter your choice: r>   r?   r?   r?   r?   r?   r?   ?   ?	   ra  ?   ?   ?   ?   ?   ?   ?   ?   ?   rq  ?   ?   )rC   rG   r?  r  r@  rz   rP   rX   r?   r?   r?   r?  r?   r?   r?   r?   r?   r	  r  r  rM  rT  rn  r?  r?  r~  r?  r?  rD  )r+  r7   r7   r;   ?	main_menu?  s?   









































?r?  )t?
subprocessZrequestsr?   rl   r?  r%  r  r?   r?   rQ  rE   Zjsonr?   r   r   r   r   r   r   r   r	   r
   Ztelethon.syncr   r   r   r   r   r   r   Ztelethon.tl.functions.channelsr   Ztelethon.tl.functions.messagesr   r   Ztelethon.tl.typesr   r   r   r   r   r   r   r   r   r   r   r    Ztelethon.tl.functions.contactsr!   r"   Ztelethon.tl.functions.photosr#   r$   r%   r&   r'   Ztelethon.errorsr(   Ztelethon.errors.rpcerrorlistr)   r*   r+   r,   r-   r.   r/   r0   Ztelethon.sessionsr1   r?  rJ   rK   r?  r@  r?  Zwi?path?exists?mkdirrD   rX   r?   r?   r?   r?   r?   r?   r?   r?   r	  r  r  rN   r  ZLIGHTGREEN_EXrr  r?   r4   r?  r3   r?  rO   rA  r  rC   rM  rT  rn  r~  r?  r?  r?  r?  r?  r?  r7   r7   r7   r;   ?<module>   s?   h $8(

v3?@-@F  (Zw=  V;k
K