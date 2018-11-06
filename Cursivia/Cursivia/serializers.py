from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    descripcion = serializers.CharField()
    eMail = serializers.EmailField()
    fechaNacimiento = serializers.DateField()
    localidad = serializers.CharField()
    fechaAlta = serializers.DateField()
    fechaBaja = serializers.DateField()
    tipo = serializers.ChoiceField(choices=Usuario.tipoUsuario)
    estado = serializers.ChoiceField(choices=Usuario.estadoUsuario)


    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Usuario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.eMail = validated_data.get('eMail', instance.eMail)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.save()
        return instance