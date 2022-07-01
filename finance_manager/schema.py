import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import superuser_required

from finance_manager.models import BudgetRequirement
from finance_manager.types import BudgetRequirementType
from finance_manager.mutations import CreateBudgetRequirement, DeleteBudgetRequirement


class Query(graphene.ObjectType):
    # admin queries
    admin_event_budget = graphene.List(BudgetRequirementType, eventId=graphene.Int())

    def resolve_admin_event_budget(self, info, eventId):
        return BudgetRequirement.objects.filter(event__pk=eventId)


class Mutation(graphene.ObjectType):
    create_budget_requirement = CreateBudgetRequirement.Field()
    delete_budget_requirement = DeleteBudgetRequirement.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
