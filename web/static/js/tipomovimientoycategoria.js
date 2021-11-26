
var categorias_1 = new Array("Selecciona la categoria", "Salario", "Remuneracion extra", "Ventas", "Otros");
var categorias_2 = new Array("Selecciona la categoria", "Alimentacion", "Transporte", "Vestimenta", "Entretenimiento", "Gastos fijos", "Otros");

var todasCategorias = [
  [],
  categorias_1,
  categorias_2,
];

function cambia_categorias(){

 	var TipoMovimiento
 	TipoMovimiento = document.formregistros.TipoMovimiento[document.formregistros.TipoMovimiento.selectedIndex].id
 	if (TipoMovimiento != 0) {
    	mis_categorias=todasCategorias[TipoMovimiento]
    	num_categorias = mis_categorias.length
    	document.formregistros.Categoria.length = num_categorias
    	for(i=0;i<num_categorias;i++){
       	document.formregistros.Categoria.options[i].Id=mis_categorias[i]
       	document.formregistros.Categoria.options[i].text=mis_categorias[i]
    	}
 	}else{
    	document.formregistros.Categoria.length = 1
    	document.formregistros.Categoria.options[0].Id = "-"
    	document.formregistros.Categoria.options[0].text = "-"
 	}
 	document.formregistros.Categoria.options[0].selected = true
}


