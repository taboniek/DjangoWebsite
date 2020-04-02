from django import forms

class SeqContentForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(attrs=
            {'placeholder': 'Plain sequence',
             'rows': 4}
        ), 
        min_length=10, 
        required=True)
    word_size = forms.IntegerField(initial=1, required=True)

    def clean_sequence(self):
        sequence = self.cleaned_data["sequence"]
        return sequence.upper()


    def clean(self):
        sequence = self.cleaned_data["sequence"]
        word_size = self.cleaned_data["word_size"]
        if sequence and word_size:
            if len(sequence) < word_size:
                raise forms.ValidationError(
                    "Sequence cannot be shorter than word size."
                )


class RevcompForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(attrs= {'placeholder': 'Paste sequence here in plain or FASTA', 'rows': 4}
        ), 
        min_length=10, 
        required=True)
    CHOICES = (('reverseComplement', 'Reverse complement'),('reverse', 'Reverse'),('complement', 'Complement'),)
    choice = forms.ChoiceField(label='Method', widget=forms.Select,choices=CHOICES)


class RandomDNAForm(forms.Form):
    generated_Sequence_Length = forms.IntegerField(min_value = 20, max_value=10000,required=True)
    a = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)
    g = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)
    c = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)
    t = forms.FloatField(min_value=0, max_value=1, initial=0.25, required=True)

    def clean(self):
        if self.cleaned_data["a"] + self.cleaned_data["c"] + self.cleaned_data["g"] + self.cleaned_data["a"] != 1:
            raise forms.ValidationError(
                    "Halko! Prawdopodobieństwo musi się równać 1!"
                ) 
