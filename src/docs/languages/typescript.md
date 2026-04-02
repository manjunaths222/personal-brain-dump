---
title: "Typescript"
---

Typescript

TypeScript = Superset of JavaScript with static typing.
Install: npm install -g typescript && tsc --init

Primitives: number, string, boolean, any, null, undefined, never, unknown
- any: disables type checking
- unknown: safer than any (must narrow before use)
- never: functions that never return (throw errors or infinite loops)

Arrays, Tuples, Enums:
```typescript
let numbers: number[] = [1, 2, 3];
let user: [string, number] = ['John', 25]; // Tuple
enum Role { Admin, User, Guest };
```

Functions:
```typescript
function add(a: number, b: number): number { return a + b; }
// Optional: func(a?: number), Default: func(a = 10), Rest: func(...args: number[])
```

Type Aliases & Interfaces:
```typescript
type User = { id: number; name: string };
interface Product { id: number; name: string; price?: number; }
```
- interface: extendable, better for OOP
- type: supports unions, intersections

Unions, Intersections, Literals:
```typescript
let id: number | string = 123;
type C = A & B; // Intersection
let status: 'success' | 'error' | 'loading';
```

Type Narrowing: typeof, instanceof, custom type guards

Generics:
```typescript
function identity<T>(value: T): T { return value; }
function logLength<T extends { length: number }>(arg: T): void { ... }
```

Classes: public, private, protected, readonly access modifiers

Advanced Types:
- Mapped Types: { readonly [K in keyof User]: User[K] }
- Conditional Types: type IsString<T> = T extends string ? true : false
- keyof, typeof, infer

Utility Types:
- Partial<T>, Required<T>, Readonly<T>
- Pick<T, K>, Omit<T, K>
- Record<K, T>, ReturnType<T>, Parameters<T>

TypeScript with React:
```typescript
type Props = { title: string };
const Header: React.FC<Props> = ({ title }) => <h1>{title}</h1>;
const [count, setCount] = useState<number>(0);
const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {}
```

tsconfig.json key options:
```json
{ "strict": true, "target": "ES6", "module": "ESNext", "noImplicitAny": true }
```

Testing: Jest with ts-jest

Best Practices:
- Prefer unknown over any
- Enable strict mode in tsconfig
- Use as const for literals
- Write reusable types : ApiResponse<T>
- Prefer readability over complex types
