---
title: "Graphql"
---

GraphQL

https://graphql.org/learn/

OVERVIEW

GraphQL Cheatsheet for Interviews

1. Basics of GraphQL
* GraphQL - A query language for APIs, enabling clients to request only the data they need.
* Key Operations:
    * Query - Fetch data
    * Mutation - Modify data
    * Subscription - Real-time updates

2. Schema Definition
A GraphQL schema defines types and operations.
type Query {
  human(id: ID!): Human
}

type Human {
  name: String
  appearsIn: [Episode]
}

enum Episode {
  NEWHOPE
  EMPIRE
  JEDI
}

3. Root Fields & Resolvers
* Root Fields: Entry points (Query, Mutation, Subscription).
* Resolvers: Functions that fetch data for fields.
Example Resolver in JavaScript
const resolvers = {
  Query: {
    human: (_, { id }) => humans.find(h => h.id === id)
  }
};

4. Types in GraphQL
Type | Description | Example
Scalar | Basic data types | String, Int, Boolean, ID, Float
Object | Custom types | type User { name: String }
List | Array of types | [String]
Enum | Fixed set of values | enum Role { ADMIN, USER }
Interface | Abstract type | interface Character { name: String }
Union | Multiple types | union SearchResult = User
Input Object | Used in mutations | input UserInput { name: String }

5. Queries & Mutations
Query:
query {
  human(id: "1002") {
    name
  }
}

Mutation:
mutation {
  createUser(name: "John") {
    id
    name
  }
}

Mutation with Input Type:
mutation {
  createUser(input: { name: "John", age: 25 }) {
    id
    name
  }
}

input ReviewInput {
  stars: Int!
  commentary: String
}
type Mutation {
  createReview(episode: Episode, review: ReviewInput!): Review
}

6. Directives
Used to modify execution behavior.
@deprecated - Marks a field as deprecated
@skip(if: Boolean) - Skips a field if true
@include(if: Boolean) - Includes a field if true

7. Subscriptions (Real-time Updates)
* Used for live updates using WebSockets.
subscription {
  newMessage {
    content
    sender
  }
}

8. Error Handling
GraphQL returns errors in a structured format.
{
  "data": { "human": null },
  "errors": [{ "message": "Human not found", "path": ["human"] }]
}
Best Practices:
* Use try-catch blocks in resolvers
* Implement custom error classes
* Partial data + errors still get returned

9. Introspection (Schema Discovery)
Get All Types in Schema:
{ __schema { types { name } } }

Check Fields of a Type:
{ __type(name: "Human") { fields { name } } }

Disable in Production:
const server = new ApolloServer({ typeDefs, resolvers, introspection: false });

10. GraphQL Best Practices
* Use Pagination for large lists (limit, cursor)
* Use DataLoader to avoid N+1 query problem
* Use Authentication & Authorization (context in resolvers)
* Monitor Performance using Apollo Tracing
* Handle Errors Properly with structured error messages

EXECUTION

GraphQL executes queries hierarchically.
Resolvers handle each field, step by step.
Independent fields execute in parallel.
GraphQL gracefully handles errors, returning partial data.

INTERFACE VS UNION VS FRAGMENT

1. Interfaces in GraphQL
An interface is an abstract type that multiple types can implement.

interface Character {
  name: String!
  appearsIn: [Episode]!
}

type Human implements Character {
  name: String!
  appearsIn: [Episode]!
  homePlanet: String
}

type Droid implements Character {
  name: String!
  appearsIn: [Episode]!
  primaryFunction: String
}

2. Unions in GraphQL
A union allows a field to return one of multiple types, but does NOT enforce common fields.
union SearchResult = Human | Droid | Starship

3. GraphQL Fragments
A fragment is a reusable query part that helps avoid repetition.

fragment CharacterFields on Character {
  name
  appearsIn
}

query {
  human(id: "1001") {
    ...CharacterFields
    homePlanet
  }
  droid(id: "2001") {
    ...CharacterFields
    primaryFunction
  }
}

Feature Comparison: Interface vs Union vs Fragment
Interface: Enforces common fields - Yes; Different return types - Yes; Requires inline fragments - No
Union: Enforces common fields - No; Different return types - Yes; Requires inline fragments - Yes
Fragment: Enforces common fields - No; Reduces query repetition - Yes

HOW IS THIS DONE?

1. GraphQL Schema:
type Query { human(id: ID!): Human }
type Human { name: String; appearsIn: [Episode]; starships: [Starship] }
enum Episode { NEWHOPE; EMPIRE; JEDI }
type Starship { name: String }

2. Sample Data:
const humans = [
  { id: "1001", name: "Luke Skywalker", appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], starshipIds: ["3001"] },
  { id: "1002", name: "Darth Vader", appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], starshipIds: ["3002"] }
];
const starships = [
  { id: "3001", name: "X-Wing" },
  { id: "3002", name: "TIE Advanced x1" }
];

3. Resolvers:
const resolvers = {
  Query: { human: (_, { id }) => humans.find(h => h.id === id) },
  Human: { starships: (parent) => starships.filter(s => parent.starshipIds.includes(s.id)) }
};

4. Apollo Server Setup + Subscriptions with PubSub for real-time messaging.
