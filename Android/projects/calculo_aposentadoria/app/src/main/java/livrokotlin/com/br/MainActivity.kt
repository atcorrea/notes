package livrokotlin.com.br

import android.app.Activity
import android.os.Bundle
import android.widget.*

class MainActivity : Activity(){

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val spn_sexo = findViewById<Spinner>(R.id.spn_sexo)
        val txt_idade = findViewById<EditText>(R.id.txt_idade)
        val btn_calcular = findViewById<Button>(R.id.btn_calcular)
        val txt_resultado = findViewById<TextView>(R.id.txt_resultado)

        spn_sexo.adapter = ArrayAdapter<String>(this, android.R.layout.simple_spinner_dropdown_item, listOf("Masculino", "Feminino"))

        btn_calcular.setOnClickListener {
            val sexo = spn_sexo.selectedItem as String
            val idade = txt_idade.text.toString().toInt()

            val resultado = calcular(sexo, idade)
            txt_resultado.text = "Faltam $resultado anos para você se aposentar."
        }
    }

    private fun calcular(sexo: String, idade:Int) :Int {
        var resultado = 0
        if (sexo == "Masculino") {
            resultado = 65 - idade
        } else {
            resultado = 60 - idade
        }

        return resultado
    }
}