from graphene_django import DjangoObjectType
import graphene
from graphene import ObjectType, Node, Schema
from lead_manager.models import Leads
import json

class LeadsType(DjangoObjectType):
    class Meta:
        model = Leads
        interfaces = (Node, )

class Query(graphene.ObjectType):
    all_leads = graphene.List(LeadsType)
    one_lead = graphene.Field(lambda: graphene.List(LeadsType), email=graphene.String(required=True))

    def resolve_all_leads(self, info, **kwargs):
        return Leads.objects.all()
    
    def resolve_one_lead(self, info, **kwargs):
        email = kwargs.get('email')

        if email is not None:
            lead = Leads.objects.get(email=email)
            return lead

class createLead(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        contacted = graphene.String(required=True)
        notes = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
    
    ok = graphene.Boolean()
    info = graphene.Field(LeadsType, required=False)

    def mutate(self, info, **input):
        print("GRAPHQL ARGS", input)
        email = input['email']
        contacted = input['contacted']
        notes = input['notes']
        first_name = input["first_name"]
        last_name = input["last_name"]

        modify = Leads(email=email,
                    contacted=contacted,
                    notes=notes,
                    first_name=first_name,
                    last_name=last_name)
        modify.save()

        return createLead(ok=True, info=modify)

class Mutation(graphene.ObjectType):
    create_Lead = createLead.Field()

schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=False)