# Android
> Android is an operating system for mobile phones, tablets, TVs and similar devices. Google bought Android in 2005 and has since made Android available for mobile phone, tablet and TV producers. The result is that popular brands like HTC, Samsung, Sony, LG, Motorola etc. as well as lots of cheaper brands are now producing phones, tablets and TVs running the Android operating system. At the time of writing more than 1 billion Android devices have been activated world wide, and around 1.5 million Android devices are activated every day.
- **Densidade de pixels**: pixels por polegada (Dp)
- É mais indicado usar DPs do que Pixels, por conta da diversidade de dispositivos e sua densidade de pixels.
- 

## Activities
- Uma **activity** é uma tela do seu aplicativo
- É um arquivo xml contendo os componentes da tela
- Este arquivo fica dentro da pasta **resources**, permitindo seu acesso programaticamente
- Para acessar os resources, você utiliza a classe **R**, que é gerada automaticamente pela IDE. (não deve ser modificada)
- Normalmente acompanhadas de um arquivo Java ou kotlin para execução (meio que um code behind)

## Layouts
- Constraint layout é baseado no conceito de constraints
- Constraint layouts permite aninhar layouts 

## Constraints
- Você precisa prender os componentes em algum lugar para eles se posicionarem corretamente na tela do app.     Os pontos presos são **constraints**.
- caso você não coloque constraints nos componentes, eles serão movidos para o topo esquerdo.

## Views
- **views** são os componentes que aparecem em uma tela, como botões, text boxes, etc.
- Para acessar os componentes no código, usa-se a chamada **R.id**:
```Java
findViewById<EditText>(R.id.editText)
```
- orientados a eventos (como webforms)
```Java
button?.setOnClickListener(object : View.OnClickListener {
            override fun onClick(v: View?) {
                numTimesClicked++
            }
        })
```

# Mais
- arquivos da pasta **res** não podem ter letras maiúsculas

## Referências:
- [Site oficial do Android](https://developer.android.com/about)
- [Android Concepts (4.4)](http://tutorials.jenkov.com/android/index.html)