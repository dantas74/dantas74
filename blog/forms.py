from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']

        labels = {
            'user_name': 'Insira seu nome',
            'email': 'Digite seu melhor email',
            'text': 'Escreva sua opinião sobre esse post'
        }

        help_texts = {
            'user_name': 'Insira um nome o qual você queira ser chamado',
            'email': 'Digite seu melhor email para que possamos entrar em contato',
            'text': 'Insira seus pensamentos, críticas ou sugestões que sempre estamos dispostos a ouvir',
        }

        error_messages = {
            'user_name': {
                'null': 'Este campo não pode ser nulo',
                'blank': 'Este campo não pode estar vazio',
                'required': 'Este campo é obrigatório',
            },
            'email': {
                'null': 'Este campo não pode ser nulo',
                'blank': 'Este campo não pode estar vazio',
                'invalid': 'Insira um email válido',
                'required': 'Este campo é obrigatório',
            },
            'text': {
                'null': 'Este campo não pode ser nulo',
                'blank': 'Este campo não pode estar vazio',
                'required': 'Este campo é obrigatório',
            }
        }
