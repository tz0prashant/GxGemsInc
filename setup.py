o
    cp�b�  �                   @   sL  d dl Z d dlmZmZ d dlmZ d dlZd dlZd dlZd dl Z d dlZd dl	Z	dZ
e�  ejZejZejZejZejZejZeeeeegZdd� Zdd� Z	 e�  e�  eed
 e � eed e � eed e � eed��Zedkr�ed� e �d� e �d� e �d� ed� ed� ed� edkr�e�  e�  e�  qQ)�    N)�init�Fore)�sleepz	@notoscamc                   C   s   t �d� tdt� d�� d S )N�clear�
zv
  ___                  ___  
 (o o)                (o o) 
(  V  ) Hacking Zone (  V  )
--m-m------------------m-m--

)�os�system�print�cy� r   r   � /storage/emulated/0/fls/setup.py�banner   s   
�r   c                   C   s&   t jdkrt �d� d S t �d� d S )N�nt�clsr   )r   �namer   r   r   r   r   �clr   s   
r   TzChoose an Option:z            [1] Setup Scriptz            [2] Exitz
 Enter your choice: �   z[+] Installing requierments ...zpip install telethon==1.24.0zpip install colorama==0.4.3zpip install requestsz[+] setup complete !z[+] now you can run any tool !z"
 Press enter to goto main menu...�   ) r   Zcoloramar   r   �timer   ZcsvZrandom�pickle�sysZscamZRESET�nZLIGHTGREEN_EXZlgZRED�rZWHITE�wZCYANr
   ZYELLOWZyeZcolorsr   r   r	   �int�input�ar   �exitr   r   r   r   �<module>   sP    



�