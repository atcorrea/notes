package livrokotlin.com.br.listadecompras

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val adapter = ArrayAdapter<String>(this, android.R.layout.simple_expandable_list_item_1)
        list_view_produtos.adapter = adapter

        btn_inserir.setOnClickListener {

            val produto = txt_produto.text.toString()

            if (produto.isNotEmpty()) {
                adapter.add(produto)
                txt_produto.text.clear()
            }
            else {
                txt_produto.error = "Preencha um valor"
            }
        }

        list_view_produtos.setOnItemLongClickListener {
            adapterView: AdapterView<*>, view: View, position: Int, id: Long ->

            val item = adapter.getItem(position)
            adapter.remove(item)
            true
        }
    }
}
