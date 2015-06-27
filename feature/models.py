from django.db import models
from django import forms

class Feat(models.Model):
    title = models.CharField(max_length=150)
    image = models.URLField(default='http://blogs-images.forbes.com/robertwood/files/2015/05/Bono.png')
    youtube_link = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Feat"
        verbose_name_plural = "Feats"

    def __str__(self):
        return self.title
		
class Rockinfo(models.Model):
    rock_name = models.CharField(max_length=200,default="ac/dc")
    rock_img = models.URLField(default='http://blogs-images.forbes.com/robertwood/files/2015/05/Bono.png')
    rank = models.IntegerField(default=0)
    about = models.CharField(max_length=1000,default="they are the best")
 
	
    def __str__(self):              
        return self.rock_name

		
class Rockvids(models.Model):
	rockername = models.ForeignKey(Rockinfo)
	vid_id1 = models.CharField(max_length=200,default="Z7JgY9zezj4")
	vid_name1 = models.CharField(max_length=300,default="Something Inside Me")
	vid_id2 = models.CharField(max_length=200,default="TABgNerEro8")
	vid_name2 = models.CharField(max_length=300,default="Moonlight Sonata")
	vid_singer_name1 = models.CharField(max_length=300,default="Jonathan Reyes Myers")
	vid_singer_name2 = models.CharField(max_length=300,default="Beethoven")
	
	def __str__(self):
		return self.vid_id1
		
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
		
class Genre(models.Model):
    genre_name = models.CharField(max_length=200,default="Rock")
    genre_img = models.URLField(default='http://blogs-images.forbes.com/robertwood/files/2015/05/Bono.png')
    genre_about = models.CharField(max_length=2000,default="This is a good genre")
 
	
    def __str__(self):              
        return self.genre_name
		
class Genrevids(models.Model):
	genrename = models.ForeignKey(Genre)
	vid_1 = models.CharField(max_length=200,default="Z7JgY9zezj4")
	vid_n1 = models.CharField(max_length=300,default="Something Inside Me")
	vid_2 = models.CharField(max_length=200,default="TABgNerEro8")
	vid_n2 = models.CharField(max_length=300,default="Moonlight Sonata")
	vid_s1 = models.CharField(max_length=300,default="Jonathan Reyes Myers")
	vid_s2 = models.CharField(max_length=300,default="Beethoven")
	
	def __str__(self):
		return self.vid_1
		
class Navers(models.Model):
	film = models.CharField(max_length=300,default="4532ssds")
	
	def __str__(self):
	 return self.film
	 
class Feedback(models.Model):
    fname = models.CharField(max_length = 25, default='unknown')
    fmail = models.EmailField(max_length = 50, default='unknown@unknown.com')
    msg = models.CharField(max_length = 200, default='no msg')

    def __str__(self):
        return self.fnamez