# API keys

Use API keys to authenticate API requests.

Stripe authenticates API requests using your account’s API keys. If a request doesn’t include a valid key, Stripe returns an [invalid request error](https://docs.stripe.com/error-handling.md#invalid-request-errors). If a request includes a deleted or expired key, Stripe returns an [authentication error](https://docs.stripe.com/error-handling.md#authentication-errors).

Use the [Developers Dashboard](https://dashboard.stripe.com/test/apikeys) to create, reveal, delete, and rotate API keys. You can access your API keys on the [API keys](https://dashboard.stripe.com/test/apikeys) tab.

> #### If you're new to Stripe
> 
> - **Keep your business safe:** Read our [best practices](https://docs.stripe.com/keys-best-practices.md) for managing keys.
- **Build and test**: Use your *sandbox (test mode) keys*. Sandbox keys start with `pk_test_` (publishable), `rk_test_` (restricted), and `sk_test_` (secret). They let you test without affecting live data.
- **When you’re ready to accept real payments**: Switch to your **live mode keys**, which start with `pk_live_`, `rk_live_`, and `sk_live_`. See [Switch to live mode](https://docs.stripe.com/keys.md#switch-to-live-mode) for instructions.
- **If you need to find a webhook signing secret**: Webhook secrets are separate from API keys. Find them in the [Webhooks](https://dashboard.stripe.com/webhooks) section of the Dashboard under each webhook endpoint.

## Key types 

When you sign up for a Stripe account, we create three types of API keys for you:

| Type | Safe to expose | Description |
| --- | --- | --- |
| Restricted API key (RAK)`rk_...` | No | API key with permissions you control. Limit the damage to your business that a bad actor could cause if they obtained your key. Create as many RAKs as you want and assign them to different parts of your application. [This guide](https://docs.stripe.com/keys/restricted-api-keys.md) explains how to configure and use RAKs. |
| Publishable API key | Yes | API key that you can put in front-end code or applications you distribute. |
| Secret API key`sk_...` | No | API key that has unrestricted permissions on all Stripe APIs. Because you can’t limit their permissions, we don’t recommend using secret keys for new use cases, and for existing integrations, we recommend migrating secret key usage to RAKs. |
| Organization API key`sk_org_...` | No | API key that works at the organization level. Same as account-level restricted or secret keys, but operates at the [organization](https://docs.stripe.com/get-started/account/orgs.md) level to manage multiple Stripe accounts at once. [This guide](https://docs.stripe.com/keys/organization-api-keys.md) explains how to configure and use organization API keys. |

We also support [managed API keys](https://docs.stripe.com/keys/managed-api-keys.md) issued by certain hosting platforms. Managed keys are secret API keys that a hosting platform delivers directly to your hosted applications. You don’t need to handle managed keys directly; your hosting provider issues and rotates them for you.

> #### Webhook signing secrets
> 
> Webhook signing secrets aren’t API keys—they’re per-webhook secrets that your webhook receiver uses to authenticate that webhooks actually came from Stripe. You can find the signing secret for each webhook endpoint in the [Webhooks](https://dashboard.stripe.com/webhooks) section of the Dashboard.

If you created your Stripe account before May 2026, you might not have any restricted API keys. We recommend creating RAKs and migrating from secret keys.

You’re responsible for managing your API keys safely. Read our guide to [best practices for protecting API keys](https://docs.stripe.com/keys-best-practices.md).

### Sandbox versus live mode 

All Stripe API requests occur in either a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) or *live mode* (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments). You can use a sandbox to test your integration and access test data, and live mode to access actual account data. Each mode has its own set of API keys, and objects in one mode aren’t accessible to the other. For example, a sandbox [product object](https://docs.stripe.com/api/products/object.md) can’t be part of a live mode payment.

| Type | When to use | Objects | How to use | Considerations |
| --- | --- | --- | --- | --- |
| Sandboxes | Use a sandbox, and its associated test API keys, as you build your integration. In a sandbox, card networks and payment providers don’t process payments. | API calls return simulated objects. For example, you can retrieve and use test `account`, `payment`, `customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription` objects. | Use [test credit cards and accounts](https://docs.stripe.com/testing.md#cards). You can’t accept real payment methods or work with real accounts. | [Identity](https://docs.stripe.com/identity.md) doesn’t perform any verification checks. Also, Connect [account objects](https://docs.stripe.com/api/accounts/object.md) don’t return sensitive fields. |
| Live mode | Use live mode, and its associated live API keys, when you’re ready to launch your integration and accept real money. In live mode, card networks and payment providers do process payments. | API calls return real objects. For example, you can retrieve and use real `account`, `payment`, `customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription` objects. | Accept real credit cards and work with customer accounts. You can accept actual payment authorizations, charges, and captures for credit cards and accounts. | Disputes have a more nuanced flow and a simpler [testing process](https://docs.stripe.com/testing.md#disputes). Also, some [payment methods](https://docs.stripe.com/payments/payment-methods.md) have a more nuanced flow and require more steps. |

## Protect your keys 

Only publishable keys are safe to expose outside your application’s backend. You’re responsible for protecting other Stripe API keys, including restricted API keys. Here are some ways you can protect your keys:

- Store sensitive keys in a secrets vault provided by your hosting platform. [This blog post](https://stripe.dev/blog/securing-stripe-api-keys-aws-automatic-rotation) offers an example. If you can’t use a secrets vault, use environment variables to provide keys to your backend applications.
- Don’t put keys in source code or configuration files checked into version control.

- [Limit keys to specific IP addresses](https://docs.stripe.com/keys.md#limit-api-secret-keys-ip-address) so only your servers can use them.

- [Rotate keys](https://docs.stripe.com/keys.md#rolling-keys) when team members with access to the keys leave your organization.
- Don’t share keys over email, chat, or other unencrypted channels.

For a comprehensive guide, see [best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md). We also maintain [a library of skills](https://github.com/stripe/ai/tree/main/skills) to help AI agents follow these best practices.

## Manage your API keys

Use the [Dashboard](https://dashboard.stripe.com/apikeys) to create, reveal, modify, delete, and rotate your API keys.

#### Create a restricted API key 

Use [restricted API keys](https://docs.stripe.com/keys/restricted-api-keys.md) (RAKs) for most use cases. Using a RAK, you can assign exactly the permissions your integration needs, reducing the damage a bad actor could cause to your business if they obtained your key.

- Follow the instructions on [Restricted API Keys](https://docs.stripe.com/keys/restricted-api-keys.md) to create a RAK, configure its permissions, and migrate from secret keys.

#### Create a secret API key 

Create an unrestricted secret API key only when your integration requires access to all Stripe APIs and resources without restriction. If a bad actor obtains your secret key, they can harm your business. We recommend using RAKs instead.

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click **Create secret key**.
2. In the dialog, enter the verification code that we send you by email or text message. If the dialog doesn’t continue automatically, click **Continue**.
3. Enter a name in the **Key name** field, then click **Create**.
4. Click the key value to copy it.
5. Save the key value. You can’t retrieve it later.
6. In the **Add a note** field, enter the location where you saved the key, then click **Done**.

### Reveal an API key

When you create a secret key in live mode, we display it once before you save it. Copy the key before saving it because you can’t reveal it later.

In live mode, you can reveal only API keys that we create for you, such as a default secret key or a key generated by a scheduled rotation. In sandbox mode, you can always see all of your API keys, including restricted and secret keys.

> Store sensitive keys in a place where you won’t lose them, such as a secrets vault provided by your platform. Don’t put keys in your application’s code.

Publishable API keys aren’t sensitive, so we show them by default and you don’t need to do anything to reveal them.

We can’t recover keys that you’ve forgotten or lost access to. If you lose a key, rotate or delete it and create another.

#### To reveal a RAK in live mode 

You can reveal only live-mode RAKs that we created for you. If you create a RAK yourself, you can’t reveal it after you’ve seen it once.

1. On the [API keys](https://dashboard.stripe.com/apikeys) tab in live mode, in the **Restricted keys** list, click **Reveal live key** for the key you want to reveal.
2. Click the key value to copy it.
3. Save the key value in your platform’s [secrets vault](https://docs.stripe.com/keys-best-practices.md#use-a-secrets-vault). If your platform doesn’t provide one, use an environment variable.
4. Click **Hide live key**.

#### To reveal a secret API key in live mode 

You can reveal only live-mode secret keys that we created for you. If you create a secret key yourself, you can’t reveal it after you’ve seen it once.

1. On the [API keys](https://dashboard.stripe.com/apikeys) tab in live mode, in the **Standard keys** list, click **Reveal live key** for the key you want to reveal.
2. Click the key value to copy it.
3. Save the key value in your platform’s [secrets vault](https://docs.stripe.com/keys-best-practices.md#use-a-secrets-vault). If your platform doesn’t provide one, use an environment variable.
4. Click **Hide live key**.
5. Click the overflow menu (⋯), then select **Edit key** for the key you want to add a note to.
6. In the **Note** field, enter the location where you saved the key, then click **Save**.

### Limit an API key to certain IP addresses 

You can limit a secret or restricted API key to a range of IP addresses, or to one or more specific IP addresses. Stripe recommends enabling IP restrictions on all live mode keys to prevent use from unauthorized locations. Use separate IP allowlists for separate keys when applicable (for example, to distinguish between staging and production environments).

IP addresses must use the IPv4 protocol, and you can specify any valid CIDR range. For example, you can specify the `100.10.38.0 - 100.10.38.255` range as `100.10.38.0/24`. All IP addresses in the range must start with `100.10.38`.

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, in the **Restricted keys** or **Standard keys** list, click the overflow menu (⋯) for the key you want to reveal.

2. Select **Manage IP restrictions** > **Limit use to a set of IP addresses**.

3. Do one of the following:

   - Enter one or more individual IP addresses in the **IP address** field.
   - For a range of IP addresses, enter the first address in the range (using Classless Inter-Domain Routing (CIDR) notation) in the **IP Address** field. Enter the network prefix size in the **CIDR** field.

4. To add another IP address or range, click **+ Add**.

5. Click **Save**.

### Change an API key’s name or note 

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click the overflow menu (⋯) for the key you want to change.
2. Select **Edit key**.
3. Do the following:
   - To change the name, enter a new name in the **Key name** field.
   - To change the note text, enter the new note text in the **Note** field.
4. Click **Save**.

### Expire an API key 

If you expire a secret API key or a restricted API key, you must create a new one and update any code that uses the expired key. Any code that uses the expired key can no longer make API calls.

> You can’t expire a publishable key.

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, in the **Restricted keys** or **Standard keys** list, click the overflow menu (⋯) for the key you want to expire.
2. Select **Expire key**.
3. In the dialog, click **Expire key**. If you no longer want to expire the key, click **Cancel**.

### Rotate an API key 

Rotating an API key revokes it and generates a replacement key that’s ready to use immediately. You can also schedule an API key to rotate after a certain time. The replacement key is named as follows:

- The replacement publishable key name is always `Publishable key`.
- The replacement secret key name is always `Secret key`.
- The replacement restricted key name is the same as the rotated key.

You can rename a secret or restricted API key by editing the key.

Rotate an API key in scenarios such as:

- If you lose a secret or restricted API key in live mode, and you can’t recover it from the Dashboard.
- If a secret or restricted API key is compromised, and you need to revoke it to block any potentially malicious API requests that might use the key.
- If a team member with access to the key leaves your organization or changes roles.
- If your policy requires rotating keys at certain intervals.

#### Rotate safely to avoid downtime

To avoid downtime during key rotation:

1. **Use the grace period**: When you rotate a key in the Dashboard, both the old and new keys work for up to 7 days. This lets you migrate gradually without downtime. If you need more than 7 days, create a new key manually, migrate to it, then expire the old one when you’re done.
2. **Roll out gradually**: If possible, use the new key from a small subset of your servers or services first, and watch your server logs for errors before deploying further.
3. **Monitor before revoking**: Before the old key expires, [check its request logs](https://docs.stripe.com/keys.md#view-request-logs), and expire it only after its request volume has been at zero for a few hours or days.

#### To rotate an API key

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click the overflow menu (⋯) for the key you want to rotate.
2. Select **Rotate key**.
3. Select an expiration date from the **Expiration** dropdown. If you choose **Now**, the old key is deleted. If you specify a time, the remaining time until the key expires displays below the key name.
4. Click **Rotate API key**.
5. Click the key value to copy it.
6. Save the key value. You can’t retrieve it later.
7. In the **Add a note** field, enter the location where you saved the key, then click **Save** or **Done**.

### Restore an API key’s access 

An API key might have its access limited if it hasn’t been used to create transfers, payouts, or update payout destinations for over 180 days. You can’t use a limited access key to create payouts and transfers or to create payout destinations. You can restore access to use the key normally or to perform a blocked action.

#### To restore access for an API key

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click the overflow menu (⋯) for the key you want to restore.
2. Select **Restore access**.
3. Click **Restore**.

## View API request logs for a key 

To [open the API request logs](https://docs.stripe.com/development/dashboard/request-logs.md), click the overflow menu (⋯) for any key, then select **View request logs**. Opening the logs redirects you to the Stripe Dashboard.

## Switch to live mode 

When you’re ready to accept real payments, use live mode API keys instead of sandbox (test) keys. On the [API keys](https://dashboard.stripe.com/apikeys) page, toggle from **sandbox mode** to **live mode**. The page now shows your live mode API keys.

> #### Complete go-live checklist
> 
> Switching API keys is only one step. Review the full [go-live checklist](https://docs.stripe.com/get-started/checklist/go-live.md) to make sure your integration is production ready.

### Publishable keys (client-side)

Copy your **live mode publishable key** (starts with `pk_live_`) and replace the `pk_test_` key in your client-side code. It’s safe to embed this key in your code or apps.

### Restricted or secret API keys (server-side)

Server-side API keys are sensitive, so review our [best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md). We recommend generating [restricted API keys](https://docs.stripe.com/keys/restricted-api-keys.md) for your server-side code to limit the damage to your business if your keys are ever exposed or compromised.

1. Before you start using a live mode key in your backend application, remove any hardcoded API keys from your code. Instead, use a [secrets vault](https://docs.stripe.com/keys-best-practices.md#use-a-secrets-vault) to supply the sandbox key, and confirm that your application still works. If your platform doesn’t provide a secrets vault, you can use an environment variable.
2. [Reveal](https://docs.stripe.com/keys.md#reveal-an-api-key) and copy your **live mode keys** (which start with `rk_live_` or `sk_live_`). Store the key value securely in your server environment.
3. Configure your server environment to supply live mode keys instead of sandbox keys to your application.

#### Webhook signing keys (server-side)

If you use webhooks, update each webhook endpoint’s URL and copy the new **signing secret** from the [Webhooks](https://dashboard.stripe.com/webhooks) section of the Dashboard.

## See also

- [Best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md)
- [Protecting against compromised API keys](https://support.stripe.com/questions/protecting-against-compromised-api-keys)
- [Why does my API key have limited access](https://support.stripe.com/questions/why-does-my-api-key-have-limited-access)
