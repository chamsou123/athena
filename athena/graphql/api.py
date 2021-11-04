import graphene

from athena.graphql.account.schema import AccountQueries


class Query(AccountQueries):
    pass


schema = graphene.Schema(Query)
