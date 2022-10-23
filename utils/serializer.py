from flask_restful import reqparse, fields


recipe_post_args = reqparse.RequestParser()
recipe_post_args.add_argument("titulo", type=str, help="Informe um título", required=True)
recipe_post_args.add_argument("ingredientes", type=str, help="Informe os ingredientes", required=True)
recipe_post_args.add_argument("preparo", type=str, help="Informe o modo de preparo", required=True)
recipe_post_args.add_argument("img", type=str, help="Informe a url da imagem", required=True)


recipe_put_args = reqparse.RequestParser()
recipe_put_args.add_argument("titulo", type=str, help="Informe um título")
recipe_put_args.add_argument("ingredientes", type=str, help="Informe os ingredientes")
recipe_put_args.add_argument("preparo", type=str, help="Informe o modo de preparo")
recipe_put_args.add_argument("img", type=str, help="Informe a url da imagem")


resource_fields = {
	'id': fields.Integer,
	'titulo': fields.String,
	'ingredientes': fields.String,
	'preparo': fields.String,
    'img': fields.String
}